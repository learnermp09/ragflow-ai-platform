"""
Verification script for the indexing pipeline.
"""

from app.core.config import settings
from app.core.exception import RAGFlowException
from app.pipelines.indexing_pipeline import IndexingPipeline


def main() -> None:
    """Verify the indexing pipeline."""

    try:
        pipeline = IndexingPipeline()

        vectorstore = pipeline.run()

        print("\nIndexing Pipeline Verification")
        print("-" * 45)

        print(
            f"Vector Store Type : {type(vectorstore).__name__}"
        )

        print(
            f"Storage Location  : "
            f"{settings.vectorstore.directory}"
        )

        print("\nPipeline executed successfully.")

    except RAGFlowException as error:
        print(error)


if __name__ == "__main__":
    main()