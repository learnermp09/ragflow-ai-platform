"""
Retrieval-Augmented Generation (RAG) chain service.

This module builds the Retrieval-Augmented Generation (RAG) pipeline by
combining the retriever, prompt template, and language model into a
single reusable LangChain retrieval chain.
"""

import sys

from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import (
    create_stuff_documents_chain,
)
from langchain_core.runnables import Runnable

from app.core.exception import RAGFlowException
from app.core.logger import logger
from app.core.prompts import RAG_PROMPT
from app.services.llm_service import LLMService
from app.services.retriever import RetrieverService


class RAGChainService:
    """Service responsible for constructing the RAG pipeline."""

    def __init__(self) -> None:
        """Initialize the RAG chain service."""

        self.retriever_service = RetrieverService()
        self.llm_service = LLMService()

    def get_chain(self) -> Runnable:
        """
        Build and return the Retrieval-Augmented Generation chain.

        Returns
        -------
        Runnable
            Configured LangChain retrieval chain.

        Raises
        ------
        RAGFlowException
            If RAG chain creation fails.
        """

        try:
            logger.info("Building RAG retrieval chain.")

            retriever = (
                self.retriever_service.get_retriever()
            )

            llm = self.llm_service.get_llm()

            document_chain = create_stuff_documents_chain(
                llm=llm,
                prompt=RAG_PROMPT,
            )

            rag_chain = create_retrieval_chain(
                retriever=retriever,
                combine_docs_chain=document_chain,
            )

            logger.info(
                "RAG retrieval chain created successfully."
            )

            return rag_chain

        except Exception as error:
            logger.exception(
                "Failed to create RAG retrieval chain."
            )

            raise RAGFlowException(
                error,
                sys,
            ) from error