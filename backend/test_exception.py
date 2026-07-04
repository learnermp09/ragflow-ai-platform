"""
Verify the custom exception class.
"""

import sys

from app.core.exception import RAGFlowException


def divide(a: int, b: int) -> float:

    try:
        return a / b

    except Exception as error:
        raise RAGFlowException(
            error,
            sys,
        )


def main() -> None:

    try:
        divide(10, 0)

    except Exception as error:
        print(error)


if __name__ == "__main__":
    main()