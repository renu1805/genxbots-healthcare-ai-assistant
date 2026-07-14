"""
GenXBots Healthcare AI Assistant

FastAPI Backend
Connects website requests to RAG chatbot pipeline.
"""

from fastapi import FastAPI
from pydantic import BaseModel

from chatbot import create_llm
from retriever import retrieve_documents


app = FastAPI(
    title="GenXBots Healthcare AI Assistant API",
    description="Healthcare Generative AI Assistant using RAG and Vertex AI",
    version="1.0"
)


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def health_check():
    return {
        "status": "GenXBots AI Assistant API running"
    }


@app.post("/chat")
def chat(request: QuestionRequest):

    question = request.question

    # Temporary response until vector database is loaded
    # Next step will connect ChromaDB

    response = {
        "question": question,
        "answer": "RAG pipeline connection in progress.",
        "sources": []
    }

    return response
