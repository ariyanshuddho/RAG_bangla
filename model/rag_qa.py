import faiss
import numpy as np
import json
import requests
from sentence_transformers import SentenceTransformer
import os

# Paths
INDEX_PATH = "data/bangla_faiss.index"
ID_PATH = "data/chunk_ids.json"
CHUNK_PATH = "data/hsc26_bangla_chunks.jsonl"

# Load chunks as dictionary
def load_chunks():
    with open(CHUNK_PATH, "r", encoding="utf-8") as f:
        return {json.loads(line)["id"]: json.loads(line)["text"] for line in f}

# Query Ollama's local HTTP API
def generate_with_ollama(prompt, model="gemma:2b"):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": model,
            "prompt": prompt,
            "stream": False
        }
    )
    print("🔍 Raw Ollama response:", response.json())  # Debug line
    return response.json()["response"]

# Answer query using RAG + Ollama
def answer_query(query, top_k=3):
    # Load FAISS index
    index = faiss.read_index(INDEX_PATH)

    # Load metadata
    with open(ID_PATH, "r", encoding="utf-8") as f:
        ids = json.load(f)
    chunks = load_chunks()

    # Embed the query
    model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
    query_vec = model.encode([query], convert_to_numpy=True)

    # Search in FAISS
    distances, indices = index.search(query_vec, top_k)

    # Get top matched chunks
    retrieved_chunks = [chunks[ids[i]] for i in indices[0]]
    context = "\n---\n".join(retrieved_chunks)

    # Compose prompt for Ollama
    prompt = f"""You are an assistant answering questions based on a textbook.
Use the following context to answer the question in Bangla or English as asked.

Context:
{context}

Question:
{query}

Answer:"""

    return generate_with_ollama(prompt)

# Interactive CLI
if __name__ == "__main__":
    print("📚 Ask a question (in Bangla or English):")
    while True:
        query = input("> ")
        if query.lower() in ['exit', 'quit']:
            break
        answer = answer_query(query)
        print("\n💡 Answer:\n", answer)
        print("-" * 50)
