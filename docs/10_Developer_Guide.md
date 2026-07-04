# Backend Development Standards

The backend follows the following engineering principles.

## 1. Configuration

All configurable values must be stored in `config.py`.

Hardcoded configuration values are not permitted.

---

## 2. Constants

Static values must be stored in `constants.py`.

Business logic should never contain repeated string literals.

---

## 3. Logging

Application logging must use the shared logger.

```
from app.core.logger import logger
```

Do not use `print()` statements for operational messages.

---

## 4. Exception Handling

Unexpected exceptions should be wrapped using the project-specific exception.

```
from app.core.exception import RAGFlowException
```

This ensures consistent error reporting throughout the application.

---

## 5. Prompt Management

Prompt templates must be maintained within `prompts.py`.

Prompt definitions should never be embedded directly into application logic.

---

## 6. Code Style

The project follows:

- PEP 8
- Modular architecture
- Single Responsibility Principle
- Consistent naming conventions
- Human-readable documentation