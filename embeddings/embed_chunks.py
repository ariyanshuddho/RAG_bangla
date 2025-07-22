import json
import os
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

def load_chunks(jsonl_path):
    chunks = []
    ids = []
    with open(jsonl_path, "r", encoding="utf-8") as f:
        for line in f:
            item = json.loads(line)
            chunks.append(item["text"])
            ids.append(item["id"])
    return ids, chunks

if __name__ == "__main__":
    chunk_file = os.path.join("data", "hsc26_bangla_chunks.jsonl")
    ids, texts = load_chunks(chunk_file)

    print("✅ Loaded", len(texts), "chunks")

    model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

    print("🔄 Generating embeddings...")
    embeddings = model.encode(texts, convert_to_numpy=True)

    print("✅ Shape of embeddings:", embeddings.shape)

    # Build FAISS index
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)

    print("✅ FAISS index built with", index.ntotal, "vectors")

    # Save
    faiss.write_index(index, "data/bangla_faiss.index")
    with open("data/chunk_ids.json", "w", encoding="utf-8") as f:
        json.dump(ids, f, ensure_ascii=False)

    print("✅ Saved index and IDs.")
