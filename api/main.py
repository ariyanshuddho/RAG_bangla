from fastapi import FastAPI
from pydantic import BaseModel
from model.rag_qa import answer_query

app = FastAPI(title="Bangla RAG QA API")

class Query(BaseModel):
    question: str

@app.get("/")
def home():
    return {"message": "RAG QA API is running ✅"}

@app.post("/ask")
def ask_question(query: Query):
    answer = answer_query(query.question)
    return {"question": query.question, "answer": answer}
