"""
Vector store service.

This module is responsible for creating, saving, and loading the FAISS
vector database used by the RAGFlow AI Platform.
"""

import sys
from pathlib import Path

from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

from app.core.config import settings
from app.core.exception import RAGFlowException
from app.core.logger import logger
from app.services.embedding_service import EmbeddingService


class VectorStoreService:
    """Service responsible for managing the FAISS vector store."""

    def __init__(self) -> None:
        """Initialize the vector store service."""

        self.vectorstore_directory = Path(
            settings.vectorstore.directory
        )

        self.embedding_service = EmbeddingService()

    def create_vectorstore(
        self,
        documents: list[Document],
    ) -> FAISS:
        """
        Create a FAISS vector store from chunked documents.

        Parameters
        ----------
        documents : list[Document]
            Chunked LangChain documents.

        Returns
        -------
        FAISS
            Initialized FAISS vector store.

        Raises
        ------
        RAGFlowException
            If vector store creation fails.
        """

        try:
            logger.info("Creating FAISS vector store.")

            if not documents:
                raise ValueError(
                    "No documents were provided for vector store creation."
                )

            embeddings = (
                self.embedding_service.get_embeddings()
            )

            vectorstore = FAISS.from_documents(
                documents=documents,
                embedding=embeddings,
            )

            logger.info(
                "FAISS vector store created with %d document chunk(s).",
                len(documents),
            )

            return vectorstore

        except Exception as error:
            logger.exception(
                "Vector store creation failed."
            )

            raise RAGFlowException(
                error,
                sys,
            ) from error

    def save_vectorstore(
        self,
        vectorstore: FAISS,
    ) -> None:
        """
        Save the vector store to disk.

        Parameters
        ----------
        vectorstore : FAISS
            FAISS vector store instance.

        Raises
        ------
        RAGFlowException
            If saving fails.
        """

        try:
            logger.info("Saving vector store.")

            self.vectorstore_directory.mkdir(
                parents=True,
                exist_ok=True,
            )

            vectorstore.save_local(
                str(self.vectorstore_directory)
            )

            logger.info(
                "Vector store saved to '%s'.",
                self.vectorstore_directory,
            )

        except Exception as error:
            logger.exception(
                "Failed to save vector store."
            )

            raise RAGFlowException(
                error,
                sys,
            ) from error

    def load_vectorstore(self) -> FAISS:
        """
        Load the FAISS vector store from disk.

        Returns
        -------
        FAISS
            Loaded FAISS vector store.

        Raises
        ------
        RAGFlowException
            If loading fails.
        """

        try:
            logger.info("Loading FAISS vector store.")

            if not self.vectorstore_directory.is_dir():
                raise FileNotFoundError(
                    f"Vector store directory not found: "
                    f"{self.vectorstore_directory}"
                )

            embeddings = (
                self.embedding_service.get_embeddings()
            )

            vectorstore = FAISS.load_local(
                folder_path=str(
                    self.vectorstore_directory
                ),
                embeddings=embeddings,
                allow_dangerous_deserialization=True,
            )

            logger.info(
                "FAISS vector store loaded successfully."
            )

            return vectorstore

        except Exception as error:
            logger.exception(
                "Failed to load vector store."
            )

            raise RAGFlowException(
                error,
                sys,
            ) from error