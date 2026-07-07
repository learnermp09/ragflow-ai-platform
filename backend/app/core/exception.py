"""
Custom exception classes used throughout the RAGFlow AI Platform.

This module provides a centralized application-specific exception that
captures detailed debugging information, including the source file,
line number, and original exception message.
"""

import sys
from types import ModuleType


def build_error_message(
    error: Exception,
    error_detail: ModuleType,
) -> str:
    """
    Build a detailed error message.

    Parameters
    ----------
    error : Exception
        Original exception.

    error_detail : ModuleType
        Typically the imported ``sys`` module used to retrieve exception
        information.

    Returns
    -------
    str
        Formatted error message.
    """

    _, _, exc_tb = error_detail.exc_info()

    if exc_tb is None:
        return str(error)

    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno

    return (
        f"Error in '{file_name}', "
        f"line {line_number}: "
        f"{error}"
    )


class RAGFlowException(Exception):
    """
    Application-specific exception.

    Wraps an original exception with additional debugging information,
    including the file name and line number where the error occurred.
    """

    def __init__(
        self,
        error: Exception,
        error_detail: ModuleType,
    ) -> None:
        """Initialize the custom exception."""

        super().__init__(str(error))

        self.message = build_error_message(
            error,
            error_detail,
        )

    def __str__(self) -> str:
        """Return the formatted error message."""

        return self.message