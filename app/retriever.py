"""
GenXBots Healthcare AI Assistant

Retriever Module

Stores document embeddings and retrieves
relevant healthcare document chunks.
"""

from langchain_community.vectorstores import Chroma


def create_vector_store(chunks, embeddings):
    """
    Create vector database from document chunks.
    """

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="./vector_db"
    )

    return vector_store


def retrieve_documents(vector_store, question, k=3):
    """
    Retrieve most relevant document chunks.
    """

    results = vector_store.similarity_search(
        question,
        k=k
    )

    return results
