"""
API integration test.

This script verifies that the FastAPI endpoints are functioning
correctly.
"""

import requests

from app.core.config import settings

BASE_URL = (
    f"http://127.0.0.1:8000"
    f"{settings.api.prefix}"
)


def test_health() -> None:
    """
    Test the health endpoint.
    """

    print("\nHealth Endpoint")
    print("-" * 60)

    try:
        response = requests.get(
            f"{BASE_URL}/health",
            timeout=30,
        )

        print(f"Status Code : {response.status_code}")
        print("Response")
        print(response.json())

    except requests.RequestException as error:
        print(f"Health endpoint test failed:\n{error}")


def test_ask() -> None:
    """
    Test the RAG question-answering endpoint.
    """

    print("\nRAG Endpoint")
    print("-" * 60)

    payload = {
        "question": "What is the American Community Survey?"
    }

    try:
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

    except requests.RequestException as error:
        print(f"RAG endpoint test failed:\n{error}")


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

    print("\nAPI verification completed.")


if __name__ == "__main__":
    main()