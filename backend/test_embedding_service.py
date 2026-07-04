"""
Verification script for the embedding service.
"""

from app.core.config import settings
from app.core.exception import RAGFlowException
from app.services.embedding_service import EmbeddingService


def main() -> None:
    """Verify the embedding service."""

    try:
        embedding_service = EmbeddingService()

        embeddings = embedding_service.get_embeddings()

        print("\nEmbedding Service Verification")
        print("-" * 45)
        print(f"Model Name           : {settings.embedding.model_name}")
        print(f"Device               : {settings.embedding.device}")
        print(
            f"Normalize Embeddings : "
            f"{settings.embedding.normalize_embeddings}"
        )

        sample_text = "Artificial Intelligence is transforming healthcare."

        vector = embeddings.embed_query(sample_text)

        print(f"Embedding Dimension  : {len(vector)}")

        print("\nVerification completed successfully.")

    except RAGFlowException as error:
        print(error)


if __name__ == "__main__":
    main()