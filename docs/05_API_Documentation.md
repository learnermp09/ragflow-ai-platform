# API Documentation

| Field | Details |
|--------|---------|
| **Project** | RAGFlow AI Platform |
| **Document** | API Documentation |
| **Version** | 1.0.0 |
| **Updated** | 05 July 2026 |
| **Prepared By** | Mrityunjay Pathak |
| **Role** | Freelance AI engineering engagement |

---

# Table of Contents

1. Overview
2. Base URL
3. Authentication
4. API Endpoints
5. Health Endpoint
6. Question Answering Endpoint
7. Request and Response Models
8. HTTP Status Codes
9. Error Handling
10. API Testing
11. Future API Enhancements
12. Conclusion

---

# 1. Overview

The RAGFlow AI Platform exposes a REST API using FastAPI.

The API allows client applications, such as the Streamlit frontend, to interact with the Retrieval-Augmented Generation (RAG) pipeline. At the current stage of the project, the API provides endpoints for application health monitoring and document-based question answering.

---

# 2. Base URL

When running locally, the API is available at:

```
http://127.0.0.1:8000/api/v1
```

All endpoints described in this document use this base URL.

---

# 3. Authentication

The current version of the API does not require authentication.

Future releases may support:

- API keys
- OAuth 2.0
- JWT authentication

---

# 4. API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/health` | Check application status |
| POST | `/ask` | Generate an answer using the RAG pipeline |

---

# 5. Health Endpoint

## Endpoint

```
GET /health
```

### Description

Returns the current status of the application.

---

### Example Request

```http
GET /api/v1/health
```

---

### Example Response

```json
{
    "status": "healthy",
    "application": "RAGFlow AI Platform"
}
```

---

### Success Response

| Status Code | Description |
|--------------|-------------|
| 200 | Application is running successfully |

---

# 6. Question Answering Endpoint

## Endpoint

```
POST /ask
```

### Description

Accepts a user question, retrieves the most relevant document chunks from the FAISS vector store, and generates an answer using the hosted Hugging Face language model.

---

### Request Body

```json
{
    "question": "What is the American Community Survey?"
}
```

---

### Example Request

```http
POST /api/v1/ask
Content-Type: application/json
```

Body

```json
{
    "question": "What is the American Community Survey?"
}
```

---

### Example Response

```json
{
    "answer": "The American Community Survey (ACS) is an annual survey conducted by the U.S. Census Bureau..."
}
```

---

### Success Response

| Status Code | Description |
|--------------|-------------|
| 200 | Answer generated successfully |

---

# 7. Request and Response Models

## QuestionRequest

| Field | Type | Required | Description |
|--------|------|----------|-------------|
| question | string | Yes | User question |

Example:

```json
{
    "question": "What is the American Community Survey?"
}
```

---

## QuestionResponse

| Field | Type | Description |
|--------|------|-------------|
| answer | string | Generated response |

Example:

```json
{
    "answer": "The American Community Survey (ACS) is..."
}
```

---

# 8. HTTP Status Codes

| Status Code | Meaning |
|--------------|---------|
| 200 | Request completed successfully |
| 400 | Invalid request |
| 422 | Request validation failed |
| 500 | Internal server error |

---

# 9. Error Handling

If an error occurs, FastAPI returns an appropriate HTTP status code along with an error message.

Example:

```json
{
    "detail": "Validation Error"
}
```

Unexpected server-side errors are handled through the project's custom exception handling and logging framework.

---

# 10. API Testing

The API can be verified using:

- Browser (Health endpoint)
- Swagger UI
- ReDoc
- Postman
- cURL
- `backend/test_api.py`

When the backend server is running, the following documentation pages are available.

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

# 11. Future API Enhancements

Future versions may include:

- User authentication
- Conversation history
- Document upload endpoint
- Metadata filtering
- Streaming responses
- Batch question processing
- Feedback endpoint
- Health metrics endpoint

---

# 12. Conclusion

The current REST API provides a simple interface for interacting with the RAGFlow AI Platform.

The API is intentionally lightweight, exposing only the endpoints required by the application while keeping the design modular and easy to extend as new features are added.

---

**Document Status:** Current

**Version:** 1.0.0

**End of Document**