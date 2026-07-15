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

from langchain_google_vertexai import VertexAIEmbeddings


def create_embedding_model():
    """
    Initialize Vertex AI embedding model.
    """

    embeddings = VertexAIEmbeddings(
    model_name="text-embedding-005",
    project="genxbots",
    location="us-central1"
)
    return embeddings
