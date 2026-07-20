"""
GenXBots Healthcare AI Assistant

Vertex AI Embedding Module
"""

from langchain_google_vertexai import VertexAIEmbeddings


def create_embedding_model():

    embeddings = VertexAIEmbeddings(
        model_name="text-embedding-005",
        project="genxbots",
        location="us-central1",
        request_parallelism=1
    )

    return embeddings
