"""
Request models.

This module defines the request schemas used by the FastAPI endpoints.
"""

from pydantic import BaseModel, Field


class QuestionRequest(BaseModel):
    """
    Request model for the RAG question-answering endpoint.
    """

    question: str = Field(
        ...,
        min_length=1,
        description="Question submitted by the user.",
        examples=[
            "What is the American Community Survey?",
        ],
    )