"""
Main FastAPI application.

This module creates and configures the FastAPI application for the
RAGFlow AI Platform.
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.routes import router
from app.core.config import settings
from app.core.logger import logger


@asynccontextmanager
async def lifespan(_app: FastAPI):
    """
    Manage application startup and shutdown lifecycle events.

    Parameters
    ----------
    _app : FastAPI
        FastAPI application instance.
    """

    logger.info(
        "%s started successfully.",
        settings.project.name,
    )

    yield

    logger.info(
        "%s stopped.",
        settings.project.name,
    )


app = FastAPI(
    title=settings.project.name,
    version=settings.project.version,
    description=(
        "Retrieval-Augmented Generation (RAG) platform built with "
        "FastAPI, LangChain, Hugging Face, and FAISS."
    ),
    lifespan=lifespan,
)

app.include_router(
    router,
    prefix=settings.api.prefix,
)