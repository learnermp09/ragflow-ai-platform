"""
Simple verification for the prompt template.
"""

from app.core.prompts import RAG_PROMPT


def main() -> None:
    """Display the prompt template."""

    print("\nPrompt Template")
    print("-" * 60)

    print(RAG_PROMPT)

    print("\nPrompt loaded successfully.")


if __name__ == "__main__":
    main()