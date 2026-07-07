"""
Vector store integration test.

This script verifies that the complete document indexing pipeline can
successfully create, save, and reload a FAISS vector store.

Running this script recreates the persisted FAISS vector store.
"""

from app.core.config import settings
from app.core.exception import RAGFlowException
from app.services.document_loader import DocumentLoader
from app.services.text_splitter import TextSplitterService
from app.services.vector_store import VectorStoreService


def main() -> None:
    """
    Verify vector store creation, persistence, and loading.
    """

    try:
        print("=" * 60)
        print("RAGFlow AI Platform")
        print("Vector Store Verification")
        print("=" * 60)

        loader = DocumentLoader()
        splitter = TextSplitterService()
        vector_service = VectorStoreService()

        documents = loader.load_documents()

        chunks = splitter.split_documents(
            documents,
        )

        vectorstore = vector_service.create_vectorstore(
            chunks,
        )

        vector_service.save_vectorstore(
            vectorstore,
        )

        loaded_vectorstore = (
            vector_service.load_vectorstore()
        )

        print("\nVerification Results")
        print("-" * 60)

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

        print(
            "\nVector store verification completed "
            "successfully."
        )

    except RAGFlowException as error:
        print(error)

    except Exception as error:
        print(error)


if __name__ == "__main__":
    main()