"""
Retriever service.

This module loads the persisted FAISS vector store and creates a reusable
LangChain retriever for similarity search.
"""
import sys

from langchain_community.vectorstores import FAISS

from app.core.config import settings
from app.core.exception import RAGFlowException
from app.core.logger import logger
from app.services.embedding_service import EmbeddingService
from app.core.constants import DEFAULT_TOP_K, DEFAULT_SEARCH_TYPE

class RetrieverService:
    """Service for loading and using the FAISS retriever."""

    def __init__(self) -> None:
        """Initialize the retriever service."""

        self.embedding_service = EmbeddingService()

    def load_vector_store(self) -> FAISS:
        """
        Load the persisted FAISS vector store.

        Returns
        -------
        FAISS
            Loaded FAISS vector database.
        """

        try:
            logger.info("Loading FAISS vector store.")

            vector_store = FAISS.load_local(
                folder_path=settings.vectorstore.directory,
                embeddings=self.embedding_service.get_embeddings(),
                allow_dangerous_deserialization=True,
            )

            logger.info("Vector store loaded successfully.")

            return vector_store

        except Exception as error:
            logger.exception("Unable to load vector store.")
            raise RAGFlowException(error, sys)

    def get_retriever(self, k: int = DEFAULT_TOP_K):
        """
        Create a retriever from the FAISS vector store.

        Parameters
        ----------
        k : int
            Number of documents to retrieve.

        Returns
        -------
        BaseRetriever
            LangChain retriever object.
        """

        try:
            vector_store = self.load_vector_store()

            retriever = vector_store.as_retriever(
                search_type=DEFAULT_SEARCH_TYPE,
                search_kwargs={"k": k},
            )

            logger.info("Retriever initialized successfully.")

            return retriever

        except Exception as error:
            logger.exception("Retriever initialization failed.")
            raise RAGFlowException(error, sys) from error