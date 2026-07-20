"""
GenXBots Healthcare AI Assistant
Document Loader Module

Purpose:
Load healthcare documents and prepare them
for Retrieval-Augmented Generation (RAG).
"""

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter


def load_pdf(file_path: str):
    """
    Load PDF document and extract text.

    Args:
        file_path: Path to PDF document

    Returns:
        List of document pages
    """

    loader = PyPDFLoader(file_path)

    documents = loader.load()

    return documents


def split_documents(documents):
    """
    Split documents into smaller chunks
    for embedding generation.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=2000,
        chunk_overlap=300
    )

    chunks = splitter.split_documents(documents)

    return chunks


def process_document(file_path: str):
    """
    Complete document processing pipeline.
    """

    documents = load_pdf(file_path)

    chunks = split_documents(documents)

    return chunks
