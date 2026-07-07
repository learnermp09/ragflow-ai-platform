"""
Text splitting service.

This module provides functionality for splitting loaded documents into
smaller chunks suitable for embedding generation and vector indexing.
"""

import sys

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

        Parameters
        ----------
        documents : list[Document]
            Documents to split.

        Returns
        -------
        list[Document]
            Chunked LangChain documents.

        Raises
        ------
        RAGFlowException
            If document splitting fails.
        """

        try:
            logger.info("Starting document splitting.")

            if not documents:
                raise ValueError(
                    "No documents were provided for splitting."
                )

            chunks = self.text_splitter.split_documents(
                documents
            )

            logger.info(
                "Created %d text chunk(s).",
                len(chunks),
            )

            return chunks

        except Exception as error:
            logger.exception(
                "Document splitting failed."
            )

            raise RAGFlowException(
                error,
                sys,
            ) from error