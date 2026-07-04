"""
Verification script for the vector store service.
"""

from app.core.config import settings
from app.core.exception import RAGFlowException
from app.services.document_loader import DocumentLoader
from app.services.text_splitter import TextSplitterService
from app.services.vector_store import VectorStoreService


def main() -> None:
    """Verify vector store creation and loading."""

    try:
        loader = DocumentLoader()
        splitter = TextSplitterService()
        vector_service = VectorStoreService()

        documents = loader.load_documents()

        chunks = splitter.split_documents(documents)

        vectorstore = vector_service.create_vectorstore(
            chunks
        )

        vector_service.save_vectorstore(vectorstore)

        loaded_vectorstore = (
            vector_service.load_vectorstore()
        )

        print("\nVector Store Verification")
        print("-" * 45)

        print(f"Documents Loaded : {len(documents)}")
        print(f"Chunks Created   : {len(chunks)}")
        print(
            f"Vector Directory : "
            f"{settings.vectorstore.directory}"
        )

        print(
            f"Vector Store Type: "
            f"{type(loaded_vectorstore).__name__}"
        )

        print("\nVerification completed successfully.")

    except RAGFlowException as error:
        print(error)


if __name__ == "__main__":
    main()