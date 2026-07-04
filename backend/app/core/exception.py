"""
Custom exception class used throughout the RAGFlow AI Platform.
"""
import sys

def build_error_message(error: Exception, error_detail: sys) -> str:
    """
    Build a detailed error message containing the file name,
    line number, and original exception.
    """

    _, _, exc_tb = error_detail.exc_info()

    file_name = exc_tb.tb_frame.f_code.co_filename

    line_number = exc_tb.tb_lineno

    return (
        f"Error in '{file_name}', "
        f"line {line_number}: "
        f"{str(error)}"
    )


class RAGFlowException(Exception):
    """Application-specific exception."""

    def __init__(self, error: Exception, error_detail: sys):

        super().__init__(str(error))

        self.message = build_error_message(
            error,
            error_detail,
        )

    def __str__(self) -> str:
        return self.message