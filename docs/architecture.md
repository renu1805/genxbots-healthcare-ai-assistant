flowchart TD

A[User] --> B[GenXBots AI Web Interface]

B --> C[FastAPI Backend API]

C --> D[Authentication and Request Validation]

D --> E[RAG Pipeline]

E --> F[Document Retriever]

F --> G[Vector Database - ChromaDB]

G --> H[Embedding Model - Sentence Transformers]

H --> I[Document Knowledge Base]

I --> J[Healthcare Documents - PDF Policies Guidelines]

E --> K[Google Vertex AI Gemini LLM]

K --> L[Response Generation]

L --> M[Answer with Source Citations]

M --> B
