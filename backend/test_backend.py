"""
Core infrastructure verification.

This script verifies that all backend foundation modules are working
correctly before the RAG pipeline is implemented.
"""

import sys

from app.core.config import settings
from app.core.constants import APP_NAME, APP_VERSION
from app.core.exception import RAGFlowException
from app.core.logger import logger
from app.core.prompts import RAG_PROMPT


def verify_configuration() -> None:
    """Verify application configuration."""

    logger.info("Verifying configuration...")

    logger.info("Project      : %s", APP_NAME)
    logger.info("Version      : %s", APP_VERSION)
    logger.info("Environment  : %s", settings.project.environment)

    logger.info("Configuration verification completed.")


def verify_prompt() -> None:
    """Verify prompt template."""

    logger.info("Verifying prompt template...")

    prompt = RAG_PROMPT.invoke(
        {
            "context": "Artificial Intelligence is transforming healthcare.",
            "input": "What is Artificial Intelligence?",
        }
    )

    logger.info("Prompt template loaded successfully.")

    print("\nPrompt Preview")
    print("-" * 60)
    print(prompt.messages[0].content)
    print("-" * 60)


def verify_exception() -> None:
    """Verify custom exception handling."""

    logger.info("Verifying exception handling...")

    try:
        _ = 10 / 0

    except Exception as error:
        logger.exception("Custom exception verification completed.")
        raise RAGFlowException(error, sys)


def main() -> None:
    """Execute backend verification."""

    logger.info("Starting backend infrastructure verification.")

    verify_configuration()

    verify_prompt()

    try:
        verify_exception()

    except RAGFlowException as error:
        logger.error(error)

    logger.info("Backend infrastructure verification completed successfully.")


if __name__ == "__main__":
    main()