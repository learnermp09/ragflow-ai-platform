"""
Centralized logging configuration for the RAGFlow AI Platform.

Every module in the application should import the shared logger
defined in this file instead of creating its own logger instance.
"""

import logging
from pathlib import Path

from app.core.config import settings
from app.core.constants import LOG_DATE_FORMAT, LOG_FORMAT


LOG_DIRECTORY = Path(settings.logging.directory)
LOG_DIRECTORY.mkdir(parents=True, exist_ok=True)

LOG_FILE = LOG_DIRECTORY / "ragflow.log"


logging.basicConfig(
    level=settings.logging.level,
    format=LOG_FORMAT,
    datefmt=LOG_DATE_FORMAT,
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler(),
    ],
)

logger = logging.getLogger("ragflow")