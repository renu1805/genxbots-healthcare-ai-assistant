from fastapi import FastAPI
from pydantic import BaseModel
from app.rag import ask_question

app = FastAPI(
    title="GenXBots Healthcare AI Assistant",
    version="1.0"
)

class QuestionRequest(BaseModel):
    question: str

@app.get("/")
def health():
    return {
        "status": "healthy",
        "service": "GenXBots Healthcare AI Assistant"
    }

@app.post("/ask")
def ask(request: QuestionRequest):
    answer = ask_question(request.question)
    return {
        "question": request.question,
        "answer": answer
    }
