"""
Prompt templates used throughout the RAGFlow AI Platform.

Keeping prompts in a single module makes them easier to maintain,
reuse, and improve without modifying application logic.
"""

from langchain_core.prompts import ChatPromptTemplate


RAG_PROMPT = ChatPromptTemplate.from_template(
    """
You are an AI assistant that answers questions only from the supplied context.

Instructions:

- Read the context carefully.
- If the answer exists in the context, provide a clear and complete response.
- If the answer cannot be found, say:
  "I don't have enough information in the provided documents."
- Do not create or assume facts.
- Keep the answer concise and accurate.

Context:
{context}

Question:
{input}

Answer:
"""
)