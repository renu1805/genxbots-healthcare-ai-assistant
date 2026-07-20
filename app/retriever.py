"""
GenXBots Healthcare AI Assistant

Retriever Module
"""

import time
from langchain_community.vectorstores import FAISS


VECTOR_DB_PATH = "./vector_db"


def create_vector_store(chunks, embeddings):

    print("Creating FAISS vector database...")

    successful_chunks = []

    batch_size = 25

    for i in range(0, len(chunks), batch_size):

        batch = chunks[i:i + batch_size]

        print(
            f"Embedding batch {i} - {i + len(batch)}"
        )

        retry = 0

        while retry < 5:
            try:
                test_vectors = embeddings.embed_documents(
                    [doc.page_content for doc in batch]
                )

                if len(test_vectors) == len(batch):
                    successful_chunks.extend(batch)
                    break

            except Exception as e:
                print(
                    f"Embedding failed. Retry {retry+1}/5"
                )
                print(e)

            retry += 1
            time.sleep(10)

    print(
        f"Successful chunks: {len(successful_chunks)}"
    )

    vector_store = FAISS.from_documents(
        documents=successful_chunks,
        embedding=embeddings
    )

    vector_store.save_local(
        VECTOR_DB_PATH
    )

    print(
        "FAISS database saved successfully"
    )

    return vector_store


def load_vector_store(embeddings):

    return FAISS.load_local(
        VECTOR_DB_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )


def retrieve_documents(vector_store, question, k=3):

    return vector_store.similarity_search(
        question,
        k=k
    )
