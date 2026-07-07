# RAGFlow AI Platform

A Retrieval-Augmented Generation (RAG) application built with **FastAPI**, **LangChain**, **Hugging Face**, **FAISS**, and **Streamlit**.

This repository is a sanitized version of a document question-answering platform developed during a freelance AI engineering project. The original application was designed to help users retrieve information from large collections of internal documents using Retrieval-Augmented Generation (RAG).

To protect client confidentiality, all proprietary documents, credentials, business-specific logic, prompts, and configuration have been removed or replaced. This repository uses publicly available U.S. Census Bureau documents together with open-source technologies while preserving the overall software architecture and engineering workflow.

---

## Project Overview

Large Language Models (LLMs) are capable of generating high-quality natural language responses, but they cannot reliably answer questions about organization-specific knowledge without additional context. Retrieval-Augmented Generation (RAG) addresses this challenge by retrieving relevant information from a document collection before passing it to the language model for response generation.

This project demonstrates an end-to-end RAG workflow that includes document ingestion, text chunking, embedding generation, vector indexing, semantic retrieval, prompt engineering, language model inference, REST API development, and a web-based user interface.

Although the sample documents in this repository are publicly available, the architecture and development approach closely reflect those used in real-world applications. The emphasis is on building a modular, maintainable, and extensible codebase that follows clean software engineering practices.

---

## Project Background

The original solution was developed as part of a freelance project involving collaboration with developers and other project stakeholders to build a modular document intelligence platform. Since the original implementation contained confidential client assets, this repository has been recreated using public datasets and open-source technologies.

The objective of sharing this project is to demonstrate the application architecture, engineering practices, and Retrieval-Augmented Generation workflow without exposing any client-specific information.

---

## Project Goals

The project was built with the following objectives:

- Build a complete Retrieval-Augmented Generation (RAG) application using modern open-source technologies.
- Develop a modular and maintainable backend following clean architecture principles.
- Implement semantic search using vector embeddings and a FAISS vector database.
- Integrate Hugging Face hosted language models for answer generation.
- Expose the RAG pipeline through RESTful APIs using FastAPI.
- Develop a simple and interactive frontend using Streamlit.
- Apply centralized configuration management, structured logging, and custom exception handling.
- Organize the codebase into reusable services, pipelines, models, and utilities for easier maintenance and future extension.
- Demonstrate software engineering practices that can be applied to production-oriented AI applications.

## Features

The current version of the project includes the following features:

### Document Processing

- Loads PDF documents from a configured directory.
- Splits large documents into smaller chunks for efficient retrieval.
- Supports document indexing using LangChain.

### Semantic Search

- Generates vector embeddings using Hugging Face embedding models.
- Stores document embeddings in a FAISS vector database.
- Retrieves the most relevant document chunks based on the user's question.

### Question Answering

- Uses Retrieval-Augmented Generation (RAG) to answer questions.
- Combines retrieved document context with a hosted Hugging Face language model.
- Returns responses based only on the retrieved document content.
- Removes internal reasoning blocks before displaying the final answer.

### REST API

- Built with FastAPI.
- Provides health check and question-answering endpoints.
- Uses request and response models for data validation.
- Includes interactive API documentation through Swagger UI.

### User Interface

- Simple web interface built with Streamlit.
- Allows users to submit questions and view generated answers.
- Displays user-friendly error messages when the backend is unavailable.

### Software Design

- Modular project structure with clearly separated components.
- Centralized configuration using Pydantic Settings.
- Structured logging for easier debugging.
- Custom exception handling across the application.
- Service-oriented architecture for better maintainability.

### Testing

- Includes verification scripts for the REST API.
- Includes verification scripts for vector store creation and loading.
- Each module was reviewed and tested during development.

## Technology Stack

The project is built using the following open-source technologies.

| Technology | Purpose |
|------------|---------|
| **Python 3.13** | Primary programming language used throughout the project. |
| **FastAPI** | Builds the REST API that exposes the RAG services. |
| **Streamlit** | Provides a simple web interface for interacting with the application. |
| **LangChain** | Orchestrates document loading, retrieval, prompt management, and the RAG pipeline. |
| **Hugging Face Inference API** | Hosts the Large Language Model used for answer generation. |
| **Hugging Face Embeddings** | Generates vector embeddings for document chunks. |
| **FAISS** | Stores and searches document embeddings using vector similarity. |
| **PyPDF** | Loads PDF documents for indexing. |
| **Pydantic Settings** | Manages application configuration and environment variables. |
| **Requests** | Sends HTTP requests from the Streamlit frontend to the FastAPI backend. |

### Development Tools

- **Visual Studio Code** – Primary development environment.
- **Git** – Version control.
- **GitHub** – Source code hosting and collaboration.
- **Virtual Environment (venv)** – Isolates project dependencies.

## Project Structure

The project is organized into separate backend and frontend components. Each module has a specific responsibility, making the code easier to understand and maintain.

```text
ragflow-ai-platform/
│
├── backend/
│   ├── app/
│   │   ├── api/                 # FastAPI route definitions
│   │   ├── core/                # Configuration, constants, logging, prompts, exceptions
│   │   ├── models/              # Request and response models
│   │   ├── pipelines/           # Document indexing pipeline
│   │   ├── services/            # Core business logic
│   │   ├── utils/               # Utility functions
│   │   └── main.py              # FastAPI application entry point
│   │
│   ├── us_census/               # Sample PDF documents
│   ├── vectorstore/             # FAISS vector database
│   ├── test_api.py              # API verification script
│   └── test_vector_store.py     # Vector store verification script
│
├── frontend/
│   └── app.py                   # Streamlit application
│
├── .env                         # Environment variables (not committed)
├── .env.example                 # Sample environment configuration
├── requirements.txt             # Project dependencies
├── README.md                    # Project documentation
└── LICENSE
```

### Folder Overview

| Folder | Description |
|---------|-------------|
| **backend/app/api** | Defines the REST API endpoints exposed by FastAPI. |
| **backend/app/core** | Contains application configuration, constants, logging, prompt templates, and custom exceptions. |
| **backend/app/models** | Defines the request and response schemas used by the API. |
| **backend/app/pipelines** | Implements the end-to-end document indexing workflow. |
| **backend/app/services** | Contains the core application logic, including document loading, embedding generation, vector store management, retrieval, and the RAG chain. |
| **backend/app/utils** | Utility functions used across the application. |
| **frontend** | Streamlit-based user interface for interacting with the RAG application. |
| **vectorstore** | Stores the generated FAISS vector database. |
| **us_census** | Contains publicly available sample documents used for indexing. |

## Architecture & Workflow

The application follows a modular architecture where each component has a specific responsibility. Instead of placing all the logic in a single file, the project separates document processing, vector indexing, retrieval, API services, and the user interface into independent modules.

This makes the application easier to understand, test, and extend.

### High-Level Architecture

```text
                        ┌──────────────────────┐
                        │   Streamlit Frontend │
                        └──────────┬───────────┘
                                   │
                                   │ HTTP Request
                                   ▼
                      ┌──────────────────────────┐
                      │      FastAPI Backend     │
                      └──────────┬───────────────┘
                                 │
                                 ▼
                     ┌──────────────────────────┐
                     │      API Endpoints       │
                     └──────────┬───────────────┘
                                 │
                                 ▼
                     ┌──────────────────────────┐
                     │       RAG Pipeline       │
                     └──────────┬───────────────┘
                                │
          ┌─────────────────────┴─────────────────────┐
          │                                           │
          ▼                                           ▼
┌──────────────────────┐                 ┌────────────────────────┐
│      Retriever       │                 │    Hugging Face LLM    │
└──────────┬───────────┘                 └────────────┬───────────┘
           │                                          │
           ▼                                          │
┌──────────────────────┐                              │
│     FAISS Index      │                              │
└──────────┬───────────┘                              │
           │                                          │
           ▼                                          │
┌──────────────────────┐                              │
│ Document Embeddings  │                              │
└──────────┬───────────┘                              │
           │                                          │
           ▼                                          ▼
      PDF Documents                         Generated Response
```

---

## Document Indexing Workflow

Before users can ask questions, the documents must be indexed.

During indexing, the application performs the following steps:

```text
PDF Documents
      │
      ▼
Load Documents
      │
      ▼
Split into Text Chunks
      │
      ▼
Generate Embeddings
      │
      ▼
Create FAISS Vector Index
      │
      ▼
Save Vector Store
```

This process is usually performed once whenever new documents are added or existing documents are updated.

---

## Question Answering Workflow

When a user submits a question, the application follows the steps below:

```text
User Question
      │
      ▼
FastAPI Endpoint
      │
      ▼
Load FAISS Vector Store
      │
      ▼
Retrieve Relevant Chunks
      │
      ▼
Build Prompt
      │
      ▼
Send Prompt to Hugging Face LLM
      │
      ▼
Clean Response
      │
      ▼
Return Answer
```

Only the most relevant document chunks are sent to the language model. This helps produce answers that are based on the indexed documents instead of relying solely on the model's general knowledge.

---

## Design Principles

Some of the design decisions followed while building the project include:

- Keeping each module focused on a single responsibility.
- Separating business logic from API endpoints.
- Managing application settings through centralized configuration.
- Using reusable service classes instead of writing duplicate code.
- Keeping the frontend independent of the backend implementation.
- Using logging and custom exception handling to simplify debugging.
- Organizing the project so that additional document loaders, vector databases, or language models can be added with minimal changes.

## Installation & Usage

Follow the steps below to set up and run the project on your local machine.

### Prerequisites

Before you begin, make sure you have the following installed:

- Python 3.13 or later
- Git
- A Hugging Face account
- A Hugging Face Access Token
- A LANGCHAIN account
- A LANGCHAIN Token

## 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/ragflow-ai-platform.git

cd ragflow-ai-platform
```

Replace `<your-username>` with your GitHub username.

---

## 2. Create a Virtual Environment

Create a virtual environment to keep the project dependencies isolated.

### Windows

```bash
python -m venv ragflow-ai-platform

ragflow-ai-platform\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv ragflow-ai-platform

source ragflow-ai-platform/bin/activate
```

---

## 3. Install Dependencies

Install all required Python packages.

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a `.env` file in the project root.

```text
HUGGINGFACEHUB_API_TOKEN=your_hugging_face_token
```

Replace `your_hugging_face_token` with your personal Hugging Face access token.

---

## 5. Add Documents

Place the PDF documents you want to index inside the following directory:

```text
backend/us_census/
```

The repository already includes publicly available sample documents from the U.S. Census Bureau for demonstration purposes.

---

## 6. Create the Vector Store

Before asking questions, the documents must be indexed.

Run the indexing pipeline to generate the FAISS vector database.

```bash
python backend/app/pipelines/indexing_pipeline.py
```

Alternatively, you can verify the complete indexing workflow using:

```bash
python backend/test_vector_store.py
```

After successful execution, a FAISS vector database will be created inside:

```text
backend/vectorstore/
```

---

## 7. Start the FastAPI Backend

From the project root, run:

```bash
uvicorn backend.app.main:app --reload
```

The backend will start at:

```text
http://127.0.0.1:8000
```

Swagger API documentation is available at:

```text
http://127.0.0.1:8000/docs
```

---

## 8. Start the Streamlit Frontend

Open a new terminal, activate the virtual environment, and run:

```bash
streamlit run frontend/app.py
```

The Streamlit application will open automatically in your default web browser.

---

## 9. Ask Questions

Once both the backend and frontend are running:

1. Open the Streamlit application.
2. Enter a question about the indexed documents.
3. Click **Submit**.
4. Review the generated answer.

---

## Verifying the Installation

You can verify that everything is working correctly by running the provided verification scripts.

### Verify the Vector Store

```bash
python backend/test_vector_store.py
```

### Verify the REST API

Ensure the FastAPI backend is running, then execute:

```bash
python backend/test_api.py
```

Both scripts should complete successfully without errors.

---

## Common Issues

### Backend connection error

Make sure the FastAPI server is running before launching the Streamlit application.

---

### Hugging Face authentication error

Verify that:

- the `.env` file exists
- the access token is valid
- the token has permission to use the selected model

---

### No documents found

Ensure that PDF files are available inside:

```text
backend/us_census/
```

before running the indexing pipeline.

## API Reference

The backend exposes a small set of REST APIs for interacting with the RAG application.

Once the FastAPI server is running, the interactive API documentation is available at:

```text
http://127.0.0.1:8000/docs
```

OpenAPI specification:

```text
http://127.0.0.1:8000/openapi.json
```

---

## Health Check

Checks whether the backend service is running.

**Endpoint**

```http
GET /api/v1/health
```

### Sample Response

```json
{
    "status": "healthy",
    "application": "RAGFlow AI Platform"
}
```

---

## Ask a Question

Retrieves relevant document context and generates an answer using the Retrieval-Augmented Generation (RAG) pipeline.

**Endpoint**

```http
POST /api/v1/ask
```

### Request Body

```json
{
    "question": "What is the American Community Survey?"
}
```

### Successful Response

```json
{
    "answer": "The American Community Survey (ACS) is an annual survey conducted by the U.S. Census Bureau..."
}
```

---

## Response Codes

| Status Code | Description |
|------------:|-------------|
| **200** | Request completed successfully. |
| **400** | Invalid request payload. |
| **404** | Endpoint not found. |
| **422** | Request validation failed. |
| **500** | Internal server error. |

---

## Testing the APIs

The repository includes a simple verification script that tests both API endpoints.

Start the FastAPI server first, then run:

```bash
python backend/test_api.py
```

The script verifies:

- Health endpoint
- Question-answering endpoint
- Response status codes
- Generated answer

---

## Example Using cURL

### Health Check

## Example Using cURL

### Health Check

#### Windows (PowerShell)

```powershell
curl.exe -X GET "http://127.0.0.1:8000/api/v1/health"
```

#### Linux / macOS

```bash
curl -X GET \
http://127.0.0.1:8000/api/v1/health
```

---

### Ask a Question

#### Windows (PowerShell)

```powershell
curl.exe -X POST "http://127.0.0.1:8000/api/v1/ask" `
-H "Content-Type: application/json" `
-d "{\"question\":\"What is the American Community Survey?\"}"
```

#### Linux / macOS

```bash
curl -X POST \
http://127.0.0.1:8000/api/v1/ask \
-H "Content-Type: application/json" \
-d '{"question":"What is the American Community Survey?"}'
```

---

## API Workflow

The question-answering endpoint performs the following steps:

1. Receives the user's question.
2. Searches the FAISS vector database for relevant document chunks.
3. Builds a prompt using the retrieved context.
4. Sends the prompt to the configured Hugging Face language model.
5. Cleans the generated response.
6. Returns the final answer to the client.

## Roadmap

The current version demonstrates the complete Retrieval-Augmented Generation (RAG) workflow. Future development will focus on improving scalability, usability, and deployment.

Planned enhancements include:

- Support for additional document formats such as Word, Markdown, and text files.
- Conversation history and multi-turn question answering.
- Metadata-based document filtering.
- Support for multiple vector databases and embedding models.
- Docker support for easier deployment.
- Cloud deployment examples.
- Automated testing using `pytest`.
- CI/CD pipeline using GitHub Actions.
- Performance optimization for larger document collections.

---

## Contributing

Thank you for your interest in this project.

If you would like to contribute:

1. Fork the repository.
2. Create a new branch for your changes.
3. Make your changes and test them.
4. Commit your code with a clear message.
5. Open a Pull Request.

If you find a bug or have suggestions for improvement, feel free to open an issue.

---

## Acknowledgements

This project makes use of several excellent open-source technologies, including:

- FastAPI
- LangChain
- Hugging Face
- FAISS
- Streamlit
- Pydantic

The sample documents included in this repository are publicly available documents from the **U.S. Census Bureau**. They are used only for demonstration purposes. All client-specific documents, prompts, configurations, and other sensitive information have been removed from this repository.

---

## License

This project is licensed under the MIT License.

You are free to use, modify, and distribute this project under the terms of the license. See the **LICENSE** file for more information.
