# Backend Technical Documentation

  Field             Details
  ----------------- ---------------------------------
  **Project**       RAGFlow AI Platform
  **Document**      Backend Technical Documentation
  **Version**       0.3.0
  **Updated**       04 July 2026
  **Prepared By**   Mrityunjay P.
  **Role**          AI Engineer

------------------------------------------------------------------------

# 1. Overview

This document describes the backend architecture implemented through
Sprint 03. The backend provides a modular and maintainable foundation
for a Retrieval-Augmented Generation (RAG) application using LangChain,
Hugging Face, and FAISS.

------------------------------------------------------------------------

# 2. Backend Architecture

    backend/
└── app/
    ├── __init__.py
    │
    ├── api/
    │   └── __init__.py
    │
    ├── core/
    │   ├── __init__.py      ← Yes
    │   ├── config.py
    │   ├── constants.py
    │   ├── exception.py
    │   ├── logger.py
    │   └── prompts.py
    │
    ├── pipeline/
    │   ├── __init__.py
    │   └── indexing_pipeline.py
    │
    ├── services/
    │   ├── __init__.py      ← Yes
    │   ├── document_loader.py
    │   ├── embedding_service.py
    │   ├── text_splitter.py
    │   └── vector_store.py
    │
    └── utils/
        └── __init__.py
------------------------------------------------------------------------

# 3. Core Modules

## Configuration

`config.py`

Responsibilities:

-   Load environment variables
-   Centralize project configuration
-   Configure embedding model
-   Configure document processing
-   Configure vector store
-   Configure logging
-   Configure LLM

------------------------------------------------------------------------

## Constants

`constants.py`

Provides application-wide constants such as:

-   Supported file types
-   Default directories
-   Log names
-   Configuration values

------------------------------------------------------------------------

## Logger

`logger.py`

Implements centralized logging.

Features:

-   Console logging
-   File logging
-   Timestamped messages
-   Common logger shared across the project

------------------------------------------------------------------------

## Exception

`exception.py`

Defines the custom `RAGFlowException` class.

Responsibilities:

-   Standardized exception handling
-   File name tracking
-   Line number tracking
-   Improved debugging

------------------------------------------------------------------------

## Prompt Templates

`prompts.py`

Stores reusable LangChain prompt templates.

------------------------------------------------------------------------

# 4. Service Layer

## Document Loader

Loads PDF documents from the configured directory.

Implementation:

-   PyPDFDirectoryLoader

Output:

-   List of LangChain Document objects

------------------------------------------------------------------------

## Text Splitter

Splits documents into chunks.

Implementation:

-   RecursiveCharacterTextSplitter

Configuration:

-   Chunk Size
-   Chunk Overlap

Output:

-   Chunked documents

------------------------------------------------------------------------

## Embedding Service

Creates the embedding model.

Implementation:

-   HuggingFaceEmbeddings

Current Model:

sentence-transformers/all-mpnet-base-v2

------------------------------------------------------------------------

## Vector Store

Creates and manages FAISS indexes.

Responsibilities:

-   Create vector store
-   Save vector store
-   Load vector store

Generated Files:

-   index.faiss
-   index.pkl

------------------------------------------------------------------------

## Indexing Pipeline

Coordinates the complete indexing workflow.

Workflow:

    PDF Documents
          │
          ▼
    Document Loader
          │
          ▼
    Text Splitter
          │
          ▼
    Embedding Service
          │
          ▼
    FAISS Vector Store
          │
          ▼
    Save Index

------------------------------------------------------------------------

# 5. Testing Strategy

Each module includes an independent verification script.

Implemented tests:

-   test_config.py
-   test_constants.py
-   test_logger.py
-   test_exception.py
-   test_prompts.py
-   test_document_loader.py
-   test_text_splitter.py
-   test_embedding_service.py
-   test_vector_store.py
-   test_indexing_pipeline.py
-   test_integration.py

------------------------------------------------------------------------

# 6. Current Pipeline Status

  Component             Status
  --------------------- ----------
  Configuration         Complete
  Constants             Complete
  Logger                Complete
  Exception             Complete
  Prompt Templates      Complete
  Document Loader       Complete
  Text Splitter         Complete
  Embedding Service     Complete
  Vector Store          Complete
  Indexing Pipeline     Complete
  Integration Testing   Complete

------------------------------------------------------------------------

# 7. Verification Summary

Latest verification confirmed:

-   42 PDF documents loaded
-   206 text chunks generated
-   Embedding model initialized successfully
-   FAISS vector database created
-   Vector index persisted to disk
-   Integration tests passed successfully

------------------------------------------------------------------------

# 8. Known Development Notes

## uv Installation

During Sprint 02 the `uv` executable was unavailable after activating
the project virtual environment because its installation directory was
missing from the PATH.

The issue was resolved by adding:

``` cmd
C:\Users\mriyu\.local\bin
```

to the user PATH environment variable.

This resolution has been documented for future project setup.

------------------------------------------------------------------------

# 9. Next Development Phase

Sprint 04 will implement:

-   Retriever Service
-   Similarity Search
-   Prompt Assembly
-   Hugging Face LLM Integration
-   Complete RAG Question Answering Pipeline

------------------------------------------------------------------------

# 10. Conclusion

The backend foundation and document indexing pipeline are complete. The
project now has a production-ready architecture capable of loading
documents, generating embeddings, creating a FAISS vector database, and
supporting retrieval functionality in the next sprint.

------------------------------------------------------------------------

**Document Status:** Current

**Version:** 0.3.0

**End of Document**
