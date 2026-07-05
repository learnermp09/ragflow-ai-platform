"""
Verification script for the LLM service.

This script initializes the Hugging Face chat model and verifies that
it can successfully generate a response.
"""

from app.core.config import settings
from app.services.llm_service import LLMService


def main() -> None:
    """Run the LLM service verification."""

    print("\nLLM Service Verification")
    print("-" * 45)

    service = LLMService()
    llm = service.get_llm()

    print(f"Repository          : {settings.llm.repository}")
    print(f"Provider            : {settings.huggingface.provider}")
    print(f"Task                : {settings.llm.task}")
    print(f"Temperature         : {settings.llm.temperature}")
    print(f"Max New Tokens      : {settings.llm.max_new_tokens}")
    print()

    question = "What is Retrieval-Augmented Generation (RAG)?"

    print("Prompt")
    print("-" * 45)
    print(question)
    print()

    print("Model Response")
    print("-" * 45)

    response = llm.invoke(question)

    print(response.content)
    print()

    print("Verification completed successfully.")


if __name__ == "__main__":
    main()