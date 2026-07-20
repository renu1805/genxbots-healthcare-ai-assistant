from app.embeddings import create_embedding_model
from app.retriever import load_vector_store, retrieve_documents
from app.gemini_model import create_llm

embeddings = create_embedding_model()

db = load_vector_store(embeddings)

docs = retrieve_documents(
    db,
    "What are CMS documentation requirements?"
)

context = "\n\n".join(
    [doc.page_content for doc in docs]
)

llm = create_llm()

answer = llm.invoke(
    f"""
Use the following CMS documents to answer.

Context:
{context}

Question:
What are CMS documentation requirements?
"""
)

print(answer.content)
