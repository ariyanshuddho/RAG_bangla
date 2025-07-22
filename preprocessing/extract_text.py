import fitz  # PyMuPDF
import os

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    full_text = ""

    for page in doc:
        full_text += page.get_text()

    doc.close()
    return full_text

if __name__ == "__main__":
    input_pdf = os.path.join("data", "hsc26_bangla.pdf")
    output_txt = os.path.join("data", "hsc26_bangla_raw.txt")

    text = extract_text_from_pdf(input_pdf)
    
    with open(output_txt, "w", encoding="utf-8") as f:
        f.write(text)
    
    print(f"✅ Text extracted and saved to {output_txt}")
