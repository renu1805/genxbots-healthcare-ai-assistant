"""
GenXBots Healthcare AI Assistant

Embedding Module

Creates vector representations of healthcare documents
for semantic search and RAG retrieval.
"""

"""
GenXBots Healthcare AI Assistant

Embedding Module

Uses Google Vertex AI embeddings for semantic search.
"""
"""
GenXBots Healthcare AI Assistant

Embedding Module

Uses Google Vertex AI embeddings for semantic search.
"""

import os

from langchain_google_vertexai import VertexAIEmbeddings


def create_embedding_model():
    """
    Initialize Vertex AI embedding model.
    """

    embeddings = VertexAIEmbeddings(
        model_name="text-embedding-005",
        project=os.getenv("GOOGLE_CLOUD_PROJECT", "genxbots"),
        location=os.getenv("GOOGLE_CLOUD_REGION", "us-central1")
    )

    return embeddings
