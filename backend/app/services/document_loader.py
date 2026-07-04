"""
Document loading service.

This module provides functionality for loading PDF documents from the
configured document directory. It serves as the entry point for the
document processing pipeline.
"""

from pathlib import Path

from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_core.documents import Document

from app.core.config import settings
from app.core.exception import RAGFlowException
from app.core.logger import logger


class DocumentLoader:
    """Service responsible for loading PDF documents."""

    def __init__(self) -> None:
        """Initialize the document loader."""

        self.document_directory = Path(settings.document.pdf_directory)

    def load_documents(self) -> list[Document]:
        """
        Load PDF documents from the configured directory.

        Returns:
            list[Document]: Loaded LangChain documents.

        Raises:
            RAGFlowException: If document loading fails.
        """

        try:
            logger.info("Starting document loading.")

            if not self.document_directory.exists():
                raise FileNotFoundError(
                    f"Directory not found: {self.document_directory}"
                )

            loader = PyPDFDirectoryLoader(str(self.document_directory))

            documents = loader.load()

            if not documents:
                raise ValueError(
                    f"No PDF documents found in {self.document_directory}"
                )

            logger.info(
                "Successfully loaded %d document(s).",
                len(documents),
            )

            return documents

        except Exception as error:
            logger.exception("Document loading failed.")
            raise RAGFlowException(error) from error