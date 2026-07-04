# Configuration Management

## Overview

The application uses a centralized configuration module to manage all configurable values.

The configuration system is implemented using **Pydantic Settings**, allowing application settings to be loaded from environment variables or the local `.env` file.

This approach eliminates scattered configuration throughout the codebase and provides a single source of truth.

---

## Configuration Structure

The configuration module is organized into the following logical groups:

- Project Settings
- Hugging Face Settings
- Embedding Settings
- Document Settings
- Vector Store Settings
- LLM Settings
- Logging Settings

These groups are exposed through the global `settings` object.

---

## Environment Variables

Currently, the following environment variable is required:

| Variable | Description |
|----------|-------------|
| `HUGGINGFACEHUB_API_TOKEN` | Hugging Face API access token |

During local development, the value is loaded from the `.env` file.

During production deployment, the value will be provided by Render through its Environment Variables configuration.

---

## Benefits

- Centralized configuration
- Reduced code duplication
- Improved maintainability
- Consistent application behavior
- Easier debugging
- Production-ready deployment support

# Backend Foundation

## Overview

Sprint 02 established the reusable backend infrastructure that will support all future development of the RAGFlow AI Platform.

The implementation follows a modular architecture where each core responsibility is isolated into its own module.

---

## Core Modules

### Configuration Management

File:

```
backend/app/core/config.py
```

Responsibilities:

- Load environment variables.
- Manage project configuration.
- Provide centralized application settings.

---

### Application Constants

File:

```
backend/app/core/constants.py
```

Responsibilities:

- Store immutable application values.
- Centralize reusable constants.
- Eliminate hardcoded values.

---

### Logging

File:

```
backend/app/core/logger.py
```

Responsibilities:

- Configure application logging.
- Write logs to both console and file.
- Provide a shared logger for all backend modules.

---

### Exception Handling

File:

```
backend/app/core/exception.py
```

Responsibilities:

- Standardize exception reporting.
- Include source file and line number.
- Improve debugging and maintainability.

---

### Prompt Management

File:

```
backend/app/core/prompts.py
```

Responsibilities:

- Store reusable LangChain prompt templates.
- Separate prompt engineering from application logic.
- Simplify future prompt maintenance.

---

## Verification

The backend foundation was validated using dedicated verification scripts for each module as well as an end-to-end infrastructure verification.

This confirms that the backend foundation is stable and ready for implementation of the Retrieval-Augmented Generation pipeline in the next sprint.