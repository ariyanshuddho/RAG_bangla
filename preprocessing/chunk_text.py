import os
import json

def clean_text(text):
    lines = text.split('\n')
    clean_lines = [line.strip() for line in lines if line.strip() != ""]
    return "\n".join(clean_lines)

def chunk_text(text, max_words=150):
    paragraphs = text.split("\n\n")
    chunks = []

    for i, para in enumerate(paragraphs):
        words = para.split()
        if len(words) <= max_words:
            chunks.append({"id": f"chunk_{i}", "text": para.strip()})
        else:
            # Split long paragraphs into smaller chunks
            for j in range(0, len(words), max_words):
                chunk_words = words[j:j + max_words]
                chunk_text = " ".join(chunk_words)
                chunks.append({"id": f"chunk_{i}_{j//max_words}", "text": chunk_text})
    
    return chunks

if __name__ == "__main__":
    raw_path = os.path.join("data", "hsc26_bangla_raw.txt")
    output_path = os.path.join("data", "hsc26_bangla_chunks.jsonl")

    with open(raw_path, "r", encoding="utf-8") as f:
        raw_text = f.read()

    print("✅ Raw text loaded. Length:", len(raw_text))

    cleaned = clean_text(raw_text)
    print("✅ Cleaned text length:", len(cleaned))

    chunks = chunk_text(cleaned)
    print("✅ Number of chunks created:", len(chunks))

    with open(output_path, "w", encoding="utf-8") as f:
        for chunk in chunks:
            f.write(json.dumps(chunk, ensure_ascii=False) + "\n")

    print(f"✅ Chunked and saved {len(chunks)} chunks to {output_path}")

