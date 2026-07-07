# User Manual

| Field | Details |
|--------|---------|
| **Project** | RAGFlow AI Platform |
| **Document** | User Manual |
| **Version** | 1.0.0 |
| **Updated** | 05 July 2026 |
| **Prepared By** | Mrityunjay Pathak |
| **Role** | Freelance AI engineering engagement |

---

# Table of Contents

1. Introduction
2. System Requirements
3. Starting the Application
4. Using the Application
5. Example Questions
6. Understanding the Response
7. Best Practices
8. Frequently Asked Questions
9. Troubleshooting
10. Conclusion

---

# 1. Introduction

The RAGFlow AI Platform allows users to ask questions about a collection of PDF documents using natural language.

Instead of manually searching through documents, users can type a question in plain English and receive an answer generated from the indexed documents.

The application consists of:

- Streamlit web interface
- FastAPI backend
- FAISS vector database
- Hugging Face hosted language model

---

# 2. System Requirements

Before using the application, make sure the following requirements are met.

- Python 3.11 or later
- Internet connection
- Hugging Face API token
- Indexed PDF documents
- FastAPI backend running
- Streamlit frontend running

---

# 3. Starting the Application

## Step 1: Start the Backend

From the project root directory, run:

```bash
cd backend

uvicorn app.main:app --reload
```

The backend will start on:

```
http://127.0.0.1:8000
```

You can verify that it is running by opening:

```
http://127.0.0.1:8000/docs
```

---

## Step 2: Start the Frontend

Open a new terminal.

Navigate to the project root directory and run:

```bash
streamlit run frontend/app.py
```

The application will normally open automatically in your default browser.

If it does not, open:

```
http://localhost:8501
```

---

# 4. Using the Application

### Step 1

Open the Streamlit application.

---

### Step 2

Type your question into the text box.

Example:

```
What is the American Community Survey?
```

---

### Step 3

Click the **Submit** button.

---

### Step 4

The application will:

1. Send your question to the FastAPI backend.
2. Retrieve the most relevant document content.
3. Generate a response using the language model.

---

### Step 5

Read the generated answer displayed on the screen.

---

# 5. Example Questions

Here are some example questions you can ask.

```
What is the American Community Survey?

Who conducts the survey?

What information does the survey collect?

How many households participate?

What is the purpose of the survey?
```

For the best results, ask questions related to the indexed documents.

---

# 6. Understanding the Response

When you submit a question, the application performs the following steps:

1. Searches the FAISS vector database for relevant document sections.
2. Combines those sections with a prompt template.
3. Sends the prompt to the Hugging Face language model.
4. Displays the generated answer.

The quality of the response depends on the information available in the indexed documents.

If the required information is not available, the application may indicate that it cannot answer the question based on the provided context.

---

# 7. Best Practices

For better results:

- Ask clear and specific questions.
- Use complete sentences whenever possible.
- Make sure the documents have been indexed before asking questions.
- Rebuild the vector database whenever the document collection changes.
- Wait for one response to finish before submitting another question.

---

# 8. Frequently Asked Questions

## Can I upload PDF files from the web interface?

No.

The current version indexes PDF files from the configured data directory.

---

## Can I ask questions outside the indexed documents?

The application is designed to answer questions using the indexed documents. Questions outside that knowledge base may not produce useful answers.

---

## Does the application save conversation history?

No.

Conversation history is not stored in the current version.

---

## Can multiple users use the application at the same time?

The current implementation is intended as a single-user demonstration application. Multi-user support may be added in a future release.

---

# 9. Troubleshooting

| Issue | Suggested Action |
|--------|------------------|
| Backend is not reachable | Verify that the FastAPI server is running |
| No answer is returned | Check that the vector database has been created |
| Response takes a long time | Verify internet connectivity and Hugging Face service availability |
| Empty response | Ensure the question relates to the indexed documents |
| Streamlit page does not open | Confirm that the Streamlit application is running |

For additional troubleshooting information, refer to the **Troubleshooting Guide**.

---

# 10. Conclusion

The RAGFlow AI Platform provides a simple way to search and interact with PDF documents using natural language.

By combining semantic search with a Large Language Model, users can quickly retrieve relevant information without manually searching through large collections of documents.

---

**Document Status:** Current

**Version:** 1.0.0

**End of Document**