"""
GenXBots Healthcare AI Assistant

Embedding Module

Creates vector representations of healthcare documents
for semantic search and RAG retrieval.
"""

from langchain_community.embeddings import HuggingFaceEmbeddings


def create_embedding_model():
    """
    Initialize embedding model.

    Converts text into numerical vectors
    for similarity search.
    """

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    return embeddings
