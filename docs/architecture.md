flowchart TB

A[Healthcare User] --> B[GenXBots AI Web Interface]

B --> C[FastAPI Backend API]

C --> D[Authentication and Request Validation]

D --> E[RAG Orchestration Engine]

E --> F[Document Retriever]

F --> G[ChromaDB Vector Database]

G --> H[Embedding Model<br/>Sentence Transformers]

H --> I[Healthcare Knowledge Base]

I --> J[Healthcare Documents<br/>PDFs Policies Guidelines]

E --> K[Google Vertex AI Gemini LLM]

K --> L[Response Generation]

L --> M[Answer with Source Citations]

M --> B
