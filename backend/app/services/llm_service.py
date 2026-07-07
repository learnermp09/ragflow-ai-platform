"""
Large Language Model (LLM) service.

This module initializes the Hugging Face hosted chat model used by the
RAGFlow AI Platform. The service provides a reusable interface for
creating and accessing the configured language model.
"""

import sys

from langchain_huggingface import (
    ChatHuggingFace,
    HuggingFaceEndpoint,
)

from app.core.config import settings
from app.core.exception import RAGFlowException
from app.core.logger import logger


class LLMService:
    """Service responsible for initializing the language model."""

    def __init__(self) -> None:
        """Initialize the LLM service."""

        self.llm: ChatHuggingFace = self.initialize_llm()

    def initialize_llm(self) -> ChatHuggingFace:
        """
        Initialize the Hugging Face hosted chat model.

        Returns
        -------
        ChatHuggingFace
            Configured Hugging Face chat model.
        """

        try:
            logger.info(
                "Initializing Hugging Face language model."
            )

            endpoint = HuggingFaceEndpoint(
                repo_id=settings.llm.repository,
                huggingfacehub_api_token=(
                    settings.huggingface.api_token
                ),
                provider=settings.huggingface.provider,
                task=settings.llm.task,
                max_new_tokens=settings.llm.max_new_tokens,
                temperature=settings.llm.temperature,
                repetition_penalty=(
                    settings.llm.repetition_penalty
                ),
            )

            llm = ChatHuggingFace(
                llm=endpoint,
            )

            logger.info(
                "Language model '%s' initialized successfully.",
                settings.llm.repository,
            )

            return llm

        except Exception as error:
            logger.exception(
                "Language model initialization failed."
            )

            raise RAGFlowException(
                error,
                sys,
            ) from error

    def get_llm(self) -> ChatHuggingFace:
        """
        Return the configured language model.

        Returns
        -------
        ChatHuggingFace
            Initialized Hugging Face chat model.
        """

        return self.llm