"""
Verify the centralized logger.
"""

from app.core.logger import logger


def main() -> None:

    logger.debug("Debug message")

    logger.info("Application started.")

    logger.warning("Sample warning.")

    logger.error("Sample error.")

    logger.critical("Sample critical error.")

    print("\nLogger verification completed.")
    print("Check logs/ragflow.log")


if __name__ == "__main__":
    main()