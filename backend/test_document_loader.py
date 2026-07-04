"""
Verification script for the document loading service.
"""

from app.core.exception import RAGFlowException
from app.services.document_loader import DocumentLoader


def main() -> None:
    """Verify document loading."""

    try:
        loader = DocumentLoader()

        documents = loader.load_documents()

        print("\nDocument Loader Verification")
        print("-" * 40)
        print(f"Documents loaded : {len(documents)}")

        if documents:
            print("\nFirst document")
            print("-" * 40)
            print(f"Source : {documents[0].metadata.get('source')}")
            print(f"Characters : {len(documents[0].page_content)}")

        print("\nVerification completed successfully.")

    except RAGFlowException as error:
        print(error)


if __name__ == "__main__":
    main()