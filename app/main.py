from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.retrieval import find_best_chunks, split_into_chunks

app = FastAPI(title="Offline Document Assistant")

# All chunks from every document added so far (kept in memory for now).
documents: list[str] = []


class DocumentIn(BaseModel):
    text: str


class QuestionIn(BaseModel):
    question: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/documents")
def add_document(doc: DocumentIn):
    chunks = split_into_chunks(doc.text)
    documents.extend(chunks)
    return {"chunks_added": len(chunks), "total_chunks": len(documents)}


@app.post("/ask")
def ask(q: QuestionIn):
    matches = find_best_chunks(q.question, documents)
    if not matches:
        raise HTTPException(status_code=404, detail="No relevant passage found")
    return {"matches": matches}