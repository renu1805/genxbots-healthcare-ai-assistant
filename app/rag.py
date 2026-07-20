from app.embeddings import create_embedding_model
from app.retriever import load_vector_store, retrieve_documents
from app.gemini_model import create_llm


embeddings = create_embedding_model()

db = load_vector_store(embeddings)

llm = create_llm()


def ask_question(question):

    docs = retrieve_documents(
        db,
        question
    )

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    answer = llm.invoke(
        f"""
Use only the following CMS documents to answer.

Context:
{context}

Question:
{question}
"""
    )

    return answer.content
