"""
API routes.

This module defines the REST API endpoints exposed by the RAGFlow AI
Platform.
"""

from fastapi import APIRouter

from app.core.exception import RAGFlowException
from app.core.logger import logger
from app.models.request_models import QuestionRequest
from app.models.response_models import QuestionResponse
from app.services.rag_chain import RAGChainService
from app.utils.response_cleaner import clean_response

router = APIRouter()

rag_service = RAGChainService()


@router.get(
    "/health",
    tags=["Health"],
)
def health_check() -> dict:
    """
    Health check endpoint.

    Returns
    -------
    dict
        API health status.
    """

    logger.info("Health check endpoint accessed.")

    return {
        "status": "healthy",
        "application": "RAGFlow AI Platform",
    }


@router.post(
    "/ask",
    response_model=QuestionResponse,
    tags=["RAG"],
)
def ask_question(
    request: QuestionRequest,
) -> QuestionResponse:
    """
    Answer a question using the RAG pipeline.

    Parameters
    ----------
    request : QuestionRequest
        User question.

    Returns
    -------
    QuestionResponse
        Generated answer.
    """

    try:
        logger.info("Received user question.")

        chain = rag_service.get_chain()

        response = chain.invoke(
            {
                "input": request.question,
            }
        )

        answer = clean_response(response["answer"])

        logger.info("Question answered successfully.")

        return QuestionResponse(
            answer=answer,
        )

    except Exception as error:
        logger.exception("Failed to process question.")
        raise RAGFlowException(error, __import__("sys"))