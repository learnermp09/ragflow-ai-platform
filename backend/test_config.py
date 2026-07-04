"""
Simple script to verify that application settings are loaded correctly.

Run:
    python backend/test_config.py
"""

from app.core.config import settings


def main() -> None:
    """Print the loaded application settings."""

    print("\nRAGFlow AI Platform Configuration")
    print("-" * 50)

    print(f"Project      : {settings.project.name}")
    print(f"Version      : {settings.project.version}")
    print(f"Environment  : {settings.project.environment}")

    print(f"Embedding    : {settings.embedding.model_name}")
    print(f"Device        : {settings.embedding.device}")

    print(f"PDF Directory : {settings.document.pdf_directory}")
    print(f"Chunk Size    : {settings.document.chunk_size}")
    print(f"Chunk Overlap : {settings.document.chunk_overlap}")

    print(f"Vector Store  : {settings.vectorstore.directory}")

    print(f"LLM           : {settings.llm.repository}")
    print(f"Provider      : {settings.huggingface.provider}")

    token = settings.huggingface.api_token
    print(f"API Token     : {token[:10]}...")

    print(f"Log Level     : {settings.logging.level}")

    print("-" * 50)
    print("Configuration loaded successfully.\n")


if __name__ == "__main__":
    main()