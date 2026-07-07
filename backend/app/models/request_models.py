"""
Request models.

This module defines the request schemas used by the FastAPI endpoints.
"""

from pydantic import BaseModel, Field


class QuestionRequest(BaseModel):
    """
    Request model for the question-answering endpoint.
    """

    question: str = Field(
        ...,
        min_length=1,
        max_length=1000,
        description="Question submitted by the user.",
        examples=[
            "What is the American Community Survey?",
        ],
    )