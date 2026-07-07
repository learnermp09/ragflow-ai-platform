"""
Response models.

This module defines the response schemas returned by the FastAPI
endpoints.
"""

from pydantic import BaseModel, Field


class QuestionResponse(BaseModel):
    """
    Response model for the question-answering endpoint.
    """

    answer: str = Field(
        ...,
        description="Answer generated for the user's question.",
        examples=[
            (
                "The American Community Survey (ACS) is an annual "
                "survey conducted by the U.S. Census Bureau."
            ),
        ],
    )