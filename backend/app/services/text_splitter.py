"""
Text splitting service.

This module provides functionality for splitting loaded documents into
smaller chunks suitable for embedding generation and vector indexing.
"""

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.core.config import settings
from app.core.exception import RAGFlowException
from app.core.logger import logger


class TextSplitterService:
    """Service responsible for splitting documents into text chunks."""

    def __init__(self) -> None:
        """Initialize the text splitter."""

        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=settings.document.chunk_size,
            chunk_overlap=settings.document.chunk_overlap,
        )

    def split_documents(
        self,
        documents: list[Document],
    ) -> list[Document]:
        """
        Split documents into smaller chunks.

        Args:
            documents: List of loaded LangChain documents.

        Returns:
            List of chunked LangChain documents.

        Raises:
            RAGFlowException:
                If document splitting fails.
        """

        try:
            logger.info("Starting document splitting.")

            chunks = self.text_splitter.split_documents(documents)

            logger.info(
                "Successfully created %d text chunks.",
                len(chunks),
            )

            return chunks

        except Exception as error:
            logger.exception("Document splitting failed.")
            raise RAGFlowException(error) from error