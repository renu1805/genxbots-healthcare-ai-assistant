"""
GenXBots Healthcare AI Assistant

Chatbot Module

Connects retrieved healthcare documents
with Google Vertex AI Gemini.
"""

from langchain_google_vertexai import ChatVertexAI
from langchain.chains import RetrievalQA


def create_llm():
    """
    Initialize Vertex AI Gemini model.
    """

    llm = ChatVertexAI(
        model="gemini-2.5-flash",
        temperature=0.2
    )

    return llm


def create_qa_chain(vector_store):
    """
    Create Retrieval-Augmented Generation pipeline.
    """

    llm = create_llm()

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vector_store.as_retriever(
            search_kwargs={"k": 3}
        ),
        return_source_documents=True
    )

    return qa_chain


def ask_question(qa_chain, question):
    """
    Ask healthcare questions
    and return AI response.
    """

    response = qa_chain.invoke(
        {"query": question}
    )

    return response
