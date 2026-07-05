"""
Verification script for the RAG chain service.
"""

from app.services.rag_chain import RAGChainService


def main() -> None:
    """Verify complete RAG pipeline."""

    print("\nRAG Chain Verification")
    print("-" * 60)

    service = RAGChainService()

    chain = service.get_chain()

    question = "Who is the President of India?"

    print("Question")
    print("-" * 60)
    print(question)

    print("\nGenerating response...\n")

    response = chain.invoke(
        {
            "input": question,
        }
    )

    print("Answer")
    print("-" * 60)

    print(response["answer"])

    print("\nVerification completed successfully.")


if __name__ == "__main__":
    main()