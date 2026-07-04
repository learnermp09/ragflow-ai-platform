"""
Embedding service.

This module initializes the Hugging Face embedding model used by the
RAGFlow AI Platform. The embedding model converts text chunks into
dense vector representations for vector database indexing.
"""

from langchain_huggingface import HuggingFaceEmbeddings

from app.core.config import settings
from app.core.exception import RAGFlowException
from app.core.logger import logger


class EmbeddingService:
    """Service responsible for creating the embedding model."""

    def __init__(self) -> None:
        """Initialize the embedding service."""

        try:
            logger.info("Initializing embedding model.")

            self.embeddings = HuggingFaceEmbeddings(
                model_name=settings.embedding.model_name,
                model_kwargs={
                    "device": settings.embedding.device,
                },
                encode_kwargs={
                    "normalize_embeddings": (
                        settings.embedding.normalize_embeddings
                    ),
                },
            )

            logger.info(
                "Embedding model initialized: %s",
                settings.embedding.model_name,
            )

        except Exception as error:
            logger.exception("Embedding model initialization failed.")
            raise RAGFlowException(error) from error

    def get_embeddings(self) -> HuggingFaceEmbeddings:
        """
        Return the configured embedding model.

        Returns:
            HuggingFaceEmbeddings: Initialized embedding model.
        """

        return self.embeddings