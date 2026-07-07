# Troubleshooting Guide

| Field | Details |
|--------|---------|
| **Project** | RAGFlow AI Platform |
| **Document** | Troubleshooting Guide |
| **Version** | 1.0.0 |
| **Updated** | 05 July 2026 |
| **Prepared By** | Mrityunjay Pathak |
| **Role** | Freelance AI engineering engagement |

---

# Table of Contents

1. Overview
2. Installation Issues
3. Backend Issues
4. Vector Database Issues
5. Hugging Face Issues
6. Frontend Issues
7. API Issues
8. Common Error Messages
9. Debugging Tips
10. Conclusion

---

# 1. Overview

This document lists common issues that may occur while setting up or running the RAGFlow AI Platform.

Most problems can be resolved by checking the project configuration, dependencies, and environment variables before investigating the application code.

---

# 2. Installation Issues

## Problem

`ModuleNotFoundError`

### Possible Cause

- Missing project dependencies
- Virtual environment not activated

### Solution

Activate the virtual environment and install the project dependencies.

```bash
uv sync
```

or

```bash
pip install -r requirements.txt
```

---

## Problem

`uv` command not found

### Possible Cause

The `uv` executable is not available in the system PATH.

### Solution

Verify the installation.

```bash
uv --version
```

If required, add the installation directory to the PATH environment variable.

---

# 3. Backend Issues

## Problem

```
ModuleNotFoundError: No module named 'app'
```

### Possible Cause

The FastAPI application was started using an incorrect module path.

### Solution

Run the backend from the project root directory.

```bash
uvicorn backend.app.main:app --reload
```

or

```bash
cd backend

uvicorn app.main:app --reload
```

---

## Problem

Backend server is not reachable.

### Possible Cause

- Uvicorn is not running.
- Wrong API URL.
- Incorrect port number.

### Solution

Start the backend server.

```bash
uvicorn backend.app.main:app --reload
```

Verify that the application is available at:

```
http://127.0.0.1:8000/docs
```

---

# 4. Vector Database Issues

## Problem

```
Failed to load vector store
```

### Possible Cause

The FAISS index has not been created.

### Solution

Run the indexing pipeline or execute the verification script.

```bash
python backend/test_vector_store.py
```

Confirm that the following files exist.

```
index.faiss

index.pkl
```

---

## Problem

Retrieved answers are unrelated to the documents.

### Possible Cause

- Vector store was created from outdated documents.
- Document collection has changed.

### Solution

Rebuild the vector database.

```bash
python backend/test_vector_store.py
```

---

# 5. Hugging Face Issues

## Problem

Authentication error

### Possible Cause

The Hugging Face API token is missing or invalid.

### Solution

Verify the `.env` file.

```text
HUGGINGFACEHUB_API_TOKEN=your_token
```

Restart the backend after updating the configuration.

---

## Problem

Model initialization failed.

### Possible Cause

- Invalid repository name
- Internet connectivity issue
- API service unavailable

### Solution

Verify the configured repository and internet connection.

---

# 6. Frontend Issues

## Problem

Unable to connect to backend.

### Possible Cause

The FastAPI server is not running.

### Solution

Start the backend before launching Streamlit.

```bash
uvicorn backend.app.main:app --reload
```

Then start the frontend.

```bash
streamlit run frontend/app.py
```

---

## Problem

Question submitted but no answer displayed.

### Possible Cause

The backend returned an error.

### Solution

Check:

- Backend console logs
- HTTP response code
- FastAPI logs

---

# 7. API Issues

## Problem

404 Not Found

### Possible Cause

Incorrect endpoint URL.

### Solution

Verify the API prefix.

Correct endpoints:

```
GET /api/v1/health

POST /api/v1/ask
```

---

## Problem

422 Unprocessable Entity

### Possible Cause

Invalid request payload.

### Solution

Ensure the request matches the expected schema.

Example:

```json
{
    "question": "What is the American Community Survey?"
}
```

---

## Problem

500 Internal Server Error

### Possible Cause

An unexpected exception occurred while processing the request.

### Solution

Review the backend logs for the complete exception details.

---

# 8. Common Error Messages

| Error | Possible Cause | Suggested Fix |
|--------|----------------|---------------|
| ModuleNotFoundError | Incorrect module path | Verify project structure |
| FileNotFoundError | Missing PDF documents | Check the data directory |
| ConnectionError | Backend not running | Start FastAPI server |
| TimeoutError | Slow model response | Retry the request |
| ValidationError | Invalid request format | Verify JSON payload |
| AuthenticationError | Invalid API token | Check Hugging Face credentials |

---

# 9. Debugging Tips

When diagnosing issues:

- Verify that the virtual environment is activated.
- Confirm that the `.env` file is correctly configured.
- Ensure the FAISS index has been created.
- Check that the backend server is running before starting the frontend.
- Review application logs for detailed error messages.
- Test the API using Swagger UI before testing the frontend.
- Run the individual verification scripts to isolate problems.

---

# 10. Conclusion

Most issues encountered during development are related to project configuration, missing dependencies, incorrect environment variables, or the backend server not running.

Following the setup instructions and verifying each component individually usually resolves these issues quickly.

---

**Document Status:** Current

**Version:** 1.0.0

**End of Document**