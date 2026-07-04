"""
Verification script for the text splitting service.
"""

from app.core.exception import RAGFlowException
from app.services.document_loader import DocumentLoader
from app.services.text_splitter import TextSplitterService


def main() -> None:
    """Verify document splitting."""

    try:
        loader = DocumentLoader()
        splitter = TextSplitterService()

        documents = loader.load_documents()

        chunks = splitter.split_documents(documents)

        print("\nText Splitter Verification")
        print("-" * 40)
        print(f"Documents loaded : {len(documents)}")
        print(f"Chunks created   : {len(chunks)}")

        if chunks:
            print("\nFirst Chunk")
            print("-" * 40)
            print(f"Source : {chunks[0].metadata.get('source')}")
            print(f"Characters : {len(chunks[0].page_content)}")

        print("\nVerification completed successfully.")

    except RAGFlowException as error:
        print(error)


if __name__ == "__main__":
    main()