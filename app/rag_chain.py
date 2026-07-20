from app.embeddings import create_embedding_model
from app.retriever import load_vector_store
from app.gemini_model import create_llm


embeddings = create_embedding_model()

db = load_vector_store(
    embeddings
)

llm = create_llm()


def ask_question(question):

    docs = db.similarity_search(
        question,
        k=3
    )

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
You are GenXBots Healthcare AI Assistant.

Use only the provided CMS documentation.

Context:
{context}

Question:
{question}

Provide a clear healthcare documentation answer.
"""

    response = llm.invoke(prompt)

    return response.content
