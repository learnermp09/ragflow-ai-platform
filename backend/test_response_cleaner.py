"""
Test response cleaner.
"""

from app.utils.response_cleaner import clean_response


def main() -> None:
    """Run response cleaner verification."""

    raw_response = """
<think>
I should think carefully.
This is internal reasoning.
</think>

The American Community Survey (ACS) is a nationwide survey.
"""

    print("\nRaw Response")
    print("-" * 60)
    print(raw_response)

    cleaned = clean_response(raw_response)

    print("\nCleaned Response")
    print("-" * 60)
    print(cleaned)


if __name__ == "__main__":
    main()