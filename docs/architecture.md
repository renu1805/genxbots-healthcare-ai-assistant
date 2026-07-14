# GenXBots Healthcare AI Assistant Architecture

## Overview

GenXBots Healthcare AI Assistant is an enterprise Generative AI application using Retrieval-Augmented Generation (RAG) architecture.

The system enables users to ask questions about healthcare documents and receive AI-generated responses grounded in trusted source documents.

---

# High-Level Architecture

```mermaid
flowchart TD

A[User] --> B[GenXBots AI Web Interface]

B --> C[FastAPI Backend API]

C --> D[Authentication & Request Validation]

D --> E[RAG Pipeline]

E --> F[Document Retriever]

F --> G[Vector Database<br/>ChromaDB]

G --> H[Embedding Model<br/>Sentence Transformers]

H --> I[Document Knowledge Base]

I --> J[Healthcare Documents<br/>PDF / Policies / Guidelines]

E --> K[Google Vertex AI Gemini LLM]

K --> L[Response Generation]

L --> M[Answer + Source Citations]

M --> B


flowchart LR

A[Healthcare Documents] --> B[Document Loader]

B --> C[Text Extraction]

C --> D[Document Chunking]

D --> E[Embedding Generation]

E --> F[Vector Database]

F --> G[Semantic Search]



sequenceDiagram

participant User
participant API
participant Retriever
participant VectorDB
participant Gemini

User->>API: Ask healthcare question

API->>Retriever: Search relevant context

Retriever->>VectorDB: Similarity search

VectorDB-->>Retriever: Relevant document chunks

Retriever->>Gemini: Question + Context

Gemini-->>API: Generated response

API-->>User: Answer with citations
