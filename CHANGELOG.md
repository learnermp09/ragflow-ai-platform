# Changelog

All notable changes to this project will be documented in this file.

The format is based on **Keep a Changelog**, and the project follows **Semantic Versioning (SemVer)**.

---

## [0.3.0] - Sprint 03

### Added

#### Document Processing Pipeline

- Added `document_loader.py` for loading PDF documents using LangChain `PyPDFDirectoryLoader`.
- Added `text_splitter.py` for document chunking using `RecursiveCharacterTextSplitter`.
- Added configurable chunk size and chunk overlap through centralized application settings.
- Added `embedding_service.py` for centralized Hugging Face embedding model initialization.
- Added support for the `sentence-transformers/all-mpnet-base-v2` embedding model.
- Added `vector_store.py` for creating, saving, and loading FAISS vector databases.
- Added `indexing_pipeline.py` to orchestrate the complete document indexing workflow.
- Added persistent FAISS vector store generation (`index.faiss` and `index.pkl`).

#### Integration

- Implemented an end-to-end indexing workflow:

  - PDF Loading
  - Document Chunking
  - Embedding Generation
  - FAISS Vector Store Creation
  - Vector Store Persistence

- Successfully indexed project documents into a searchable FAISS vector database.

#### Testing

- Added `test_document_loader.py`.
- Added `test_text_splitter.py`.
- Added `test_embedding_service.py`.
- Added `test_vector_store.py`.
- Added `test_indexing_pipeline.py`.
- Added `test_integration.py` for end-to-end pipeline verification.

#### Documentation

- Added Sprint 03 documentation.
- Added Day 03 development log.
- Updated backend technical documentation.
- Updated project architecture documentation.
- Documented the complete indexing pipeline workflow.
- Added verification results for document loading, chunking, embedding generation, and vector indexing.

---

## [0.2.0] - Sprint 02

### Added

#### Backend Foundation

- Introduced centralized configuration management using Pydantic Settings.
- Added automatic environment variable loading from the `.env` file.
- Added modular configuration classes for:
  - Project
  - Hugging Face
  - Embedding Model
  - Document Processing
  - Vector Store
  - Large Language Model (LLM)
  - Logging

#### Core Modules

- Added `config.py` for centralized application configuration.
- Added `constants.py` for reusable application constants.
- Added `logger.py` for centralized logging across the backend.
- Added `exception.py` containing the custom `RAGFlowException`.
- Added `prompts.py` for centralized LangChain prompt templates.

#### Testing

- Added `test_config.py`.
- Added `test_constants.py`.
- Added `test_logger.py`.
- Added `test_exception.py`.
- Added `test_prompts.py`.
- Added `test_backend.py` for backend infrastructure verification.

#### Documentation

- Updated Sprint 02 documentation.
- Updated backend documentation.
- Updated developer guide.
- Updated Day 02 development log.
- Documented the `uv` installation and PATH troubleshooting process for future project setup.

---

## [0.1.0] - Sprint 01

### Added

#### Project Initialization

- Created GitHub repository.
- Cloned the repository to the local development environment.
- Initialized the project using `uv`.
- Configured the Conda development environment.
- Added project dependencies using `uv`.
- Created the initial project directory structure.
- Added the project documentation framework.
- Created project configuration files.
- Added `.env` support.
- Added `requirements.txt` for deployment compatibility.
- Completed the initial GitHub commit.

---