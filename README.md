# GenXBots Healthcare AI Assistant

Enterprise Generative AI assistant using RAG architecture.

## Business Problem

Healthcare organizations manage thousands of documents...

## Solution

AI-powered knowledge assistant that allows users to ask questions...

## Architecture

```mermaid
flowchart TD

User[User] --> Web[GenXBots AI Web Interface]
Web --> API[FastAPI Backend API]
API --> Auth[Authentication and Validation]
Auth --> RAG[RAG Pipeline]

RAG --> Retriever[Document Retriever]
Retriever --> VectorDB[ChromaDB Vector Database]

VectorDB --> Embeddings[Sentence Transformer Embeddings]
Embeddings --> Docs[Healthcare Knowledge Base]

Docs --> Files[Healthcare Documents]

RAG --> Gemini[Google Vertex AI Gemini LLM]

Gemini --> Response[Generated Answer]
Response --> Citation[Source Citations]

Citation --> Web
```



```mermaid
sequenceDiagram

participant User
participant API
participant RAG
participant DB
participant LLM

User->>API: Ask question

API->>RAG: Process request

RAG->>DB: Search documents

DB-->>RAG: Return context

RAG->>LLM: Question + context

LLM-->>API: Generate answer

API-->>User: Response with citations
```

```mermaid
sequenceDiagram

participant User
participant API
participant RAG
participant DB
participant LLM

User->>API: Ask question

API->>RAG: Process request

RAG->>DB: Search documents

DB-->>RAG: Return context

RAG->>LLM: Question + context

LLM-->>API: Generate answer

API-->>User: Response with citations
```

## Future Roadmap

- Enterprise authentication
- Multi-document support
- Analytics dashboard

## Technology Stack

- Vertex AI Gemini
- LangChain
- ChromaDB
- FastAPI
- Docker

## AI Workflow

Document → Embeddings → Vector Search → Gemini → Response

## Responsible AI

- HIPAA considerations
- Source citations
- Hallucination reduction
