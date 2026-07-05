"""
API integration test.

This script verifies that the FastAPI endpoints are functioning
correctly.
"""

import requests

BASE_URL = "http://127.0.0.1:8000"


def test_health() -> None:
    """
    Test the health endpoint.
    """

    print("\nHealth Endpoint")
    print("-" * 60)

    response = requests.get(f"{BASE_URL}/health", timeout=30)

    print(f"Status Code : {response.status_code}")
    print("Response")
    print(response.json())


def test_ask() -> None:
    """
    Test the RAG question-answering endpoint.
    """

    print("\nRAG Endpoint")
    print("-" * 60)

    payload = {
        "question": "What is the American Community Survey?"
    }

    response = requests.post(
        f"{BASE_URL}/ask",
        json=payload,
        timeout=120,
    )

    print(f"Status Code : {response.status_code}")

    if response.status_code == 200:
        print("\nAnswer")
        print("-" * 60)
        print(response.json()["answer"])
    else:
        print("\nError")
        print(response.text)


def main() -> None:
    """
    Execute all API verification tests.
    """

    print("=" * 60)
    print("RAGFlow AI Platform")
    print("FastAPI Endpoint Verification")
    print("=" * 60)

    test_health()

    test_ask()

    print("\nVerification completed successfully.")


if __name__ == "__main__":
    main()