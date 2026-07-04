"""
Backend entry point for the RAGFlow AI Platform.

This module initializes the backend application and verifies that the
core infrastructure has been configured correctly.
"""

import sys

from app.core.config import settings
from app.core.constants import APP_NAME, APP_VERSION
from app.core.exception import RAGFlowException
from app.core.logger import logger


def initialize_application() -> None:
    """
    Initialize the backend application.
    """

    logger.info("Starting application...")

    logger.info("Project Name : %s", APP_NAME)

    logger.info("Version      : %s", APP_VERSION)

    logger.info("Environment  : %s", settings.project.environment)

    logger.info("Configuration loaded successfully.")

    logger.info("Application initialized successfully.")


def main() -> None:
    """
    Application entry point.
    """

    try:
        initialize_application()

    except Exception as error:
        logger.exception("Application startup failed.")
        raise RAGFlowException(error, sys)


if __name__ == "__main__":
    main()