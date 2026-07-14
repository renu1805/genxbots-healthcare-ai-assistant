"""
GenXBots Healthcare AI Assistant

FastAPI Backend

Provides API endpoints for chatbot interaction.
"""

from fastapi import FastAPI
from pydantic import BaseModel

from chatbot import create_qa_chain, ask_question


app = FastAPI(
    title="GenXBots Healthcare AI Assistant API",
    description="Generative AI healthcare assistant powered by RAG and Vertex AI",
    version="1.0"
)


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def health_check():
    return {
        "status": "GenXBots AI Assistant is running"
    }


@app.post("/chat")
def chat(request: QuestionRequest):

    # Placeholder response until vector database is connected

    return {
        "question": request.question,
        "answer": "AI response will be generated using Vertex AI Gemini.",
        "source": []
    }
