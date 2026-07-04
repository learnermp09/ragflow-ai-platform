# Changelog

All notable changes to this project will be documented in this file.

The format is based on **Keep a Changelog**, and the project follows **Semantic Versioning (SemVer)**.

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

---

## [0.1.0] - Sprint 01

### Added

#### Project Initialization

- Created GitHub repository.
- Cloned repository to the local development environment.
- Initialized the project using `uv`.
- Configured the Conda development environment.
- Added project dependencies using `uv`.
- Created the initial project directory structure.
- Added project documentation framework.
- Created project configuration files.
- Added `.env` support.
- Added `requirements.txt` for deployment compatibility.
- Completed the initial GitHub commit.

---