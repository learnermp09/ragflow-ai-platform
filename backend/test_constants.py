"""
Simple verification for application constants.

Run:
    python backend/test_constants.py
"""

from app.core import constants


def main() -> None:
    """Display constant values."""

    print("\nApplication Constants")
    print("-" * 50)

    print(f"Application : {constants.APP_NAME}")
    print(f"Version     : {constants.APP_VERSION}")
    print(f"API Prefix  : {constants.API_PREFIX}")

    print(f"Documents   : {constants.DOCUMENT_DIRECTORY}")
    print(f"VectorStore : {constants.VECTORSTORE_DIRECTORY}")

    print(f"Embedding   : {constants.EMBEDDING_MODEL}")
    print(f"LLM         : {constants.LLM_REPOSITORY}")

    print("\nConstants loaded successfully.")


if __name__ == "__main__":
    main()