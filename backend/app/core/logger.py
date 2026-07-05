"""
Centralized application logger.

This module configures the project-wide logger used throughout the
RAGFlow AI Platform.
"""

import logging

from app.core.config import settings
from app.core.constants import LOG_DATE_FORMAT, LOG_FORMAT

logger = logging.getLogger("ragflow")

if not logger.handlers:
    logger.setLevel(settings.logging.level)

    console_handler = logging.StreamHandler()

    formatter = logging.Formatter(
        fmt=LOG_FORMAT,
        datefmt=LOG_DATE_FORMAT,
    )

    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)

    logger.propagate = False


# Silence noisy third-party libraries
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("httpcore").setLevel(logging.WARNING)
logging.getLogger("huggingface_hub").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)