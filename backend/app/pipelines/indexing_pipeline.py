"""
Document indexing pipeline.

This module orchestrates the complete indexing workflow of the
RAGFlow AI Platform.

Pipeline:

Load Documents
        │
        ▼
Split Documents
        │
        ▼
Create Embeddings
        │
        ▼
Build FAISS Index
        │
        ▼
Save Vector Store
"""

from langchain_community.vectorstores import FAISS

from app.core.exception import RAGFlowException
from app.core.logger import logger
from app.services.document_loader import DocumentLoader
from app.services.text_splitter import TextSplitterService
from app.services.vector_store import VectorStoreService


class IndexingPipeline:
    """Pipeline responsible for indexing project documents."""

    def __init__(self) -> None:
        """Initialize indexing pipeline."""

        self.document_loader = DocumentLoader()
        self.text_splitter = TextSplitterService()
        self.vector_store = VectorStoreService()

    def run(self) -> FAISS:
        """
        Execute the complete indexing pipeline.

        Returns
        -------
        FAISS
            Generated vector database.
        """

        try:
            logger.info("Starting indexing pipeline.")

            documents = self.document_loader.load_documents()

            chunks = self.text_splitter.split_documents(
                documents
            )

            vectorstore = self.vector_store.create_vectorstore(
                chunks
            )

            self.vector_store.save_vectorstore(
                vectorstore
            )

            logger.info(
                "Indexing pipeline completed successfully."
            )

            return vectorstore

        except Exception as error:
            logger.exception(
                "Indexing pipeline failed."
            )
            raise RAGFlowException(error) from error