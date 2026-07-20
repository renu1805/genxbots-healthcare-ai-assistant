"""
GenXBots Healthcare AI Assistant

Gemini Model Configuration
"""

import os

from langchain_google_vertexai import ChatVertexAI


def create_llm():

    return ChatVertexAI(
        model="gemini-2.5-flash",
        project=os.getenv("GOOGLE_CLOUD_PROJECT", "genxbots"),
        location=os.getenv("GOOGLE_CLOUD_REGION", "us-central1"),
        temperature=0
    )
