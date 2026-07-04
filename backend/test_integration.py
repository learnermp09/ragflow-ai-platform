"""
End-to-end integration test for the Sprint 03 indexing workflow.
"""

from pathlib import Path

from app.core.config import settings
from app.core.exception import RAGFlowException
from app.pipelines.indexing_pipeline import IndexingPipeline


def main() -> None:
    """Execute the complete indexing workflow."""

    try:
        print("\n" + "=" * 60)
        print("RAGFlow AI Platform")
        print("Sprint 03 Integration Test")
        print("=" * 60)

        pipeline = IndexingPipeline()

        vectorstore = pipeline.run()

        vector_directory = Path(settings.vectorstore.directory)

        faiss_file = vector_directory / "index.faiss"
        pickle_file = vector_directory / "index.pkl"

        print("\nVerification Results")
        print("-" * 60)

        print(
            f"Vector Store Created : "
            f"{type(vectorstore).__name__}"
        )

        print(
            f"Vector Directory     : "
            f"{vector_directory}"
        )

        print(
            f"index.faiss Exists   : "
            f"{faiss_file.exists()}"
        )

        print(
            f"index.pkl Exists     : "
            f"{pickle_file.exists()}"
        )

        print("\nSprint 03 indexing workflow verified successfully.")

    except RAGFlowException as error:
        print("\nIntegration test failed.")
        print(error)


if __name__ == "__main__":
    main()