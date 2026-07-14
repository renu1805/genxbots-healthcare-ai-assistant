"""
GenXBots Healthcare AI Assistant

Knowledge Base Builder

Processes healthcare documents and creates
a searchable vector database.
"""

from document_loader import process_document
from embeddings import create_embedding_model
from retriever import create_vector_store


def build_database(document_path):

    print("Loading documents...")

    chunks = process_document(document_path)

    print(
        f"Created {len(chunks)} document chunks"
    )


    print("Creating embeddings...")

    embeddings = create_embedding_model()


    print("Building vector database...")

    vector_store = create_vector_store(
        chunks,
        embeddings
    )


    print("Knowledge base created successfully!")

    return vector_store


if __name__ == "__main__":

    build_database(
        "data/sample_healthcare_policy.pdf"
    )
