"""
Verification script for the retriever service.
"""

from app.services.retriever import RetrieverService


def main() -> None:
    """Verify retriever initialization."""

    service = RetrieverService()

    retriever = service.get_retriever()

    documents = retriever.invoke(
        "What is the American Community Survey?"
    )

    print()
    print("Retriever Verification")
    print("-" * 45)

    print(f"Retrieved Documents : {len(documents)}")
    print()

    if documents:
        first = documents[0]

        print("First Retrieved Document")
        print("-" * 45)
        print(f"Source : {first.metadata.get('source')}")
        print(f"Characters : {len(first.page_content)}")
        print()
        print("Preview")
        print("-" * 45)
        print(first.page_content[:500])

    print()
    print("Verification completed successfully.")


if __name__ == "__main__":
    main()