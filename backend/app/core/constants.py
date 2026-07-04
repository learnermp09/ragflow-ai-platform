"""
Application-wide constant values.

Constants defined here remain unchanged during runtime and are shared
across different modules of the application.
"""

APP_NAME = "RAGFlow AI Platform"
APP_VERSION = "1.0.0"

API_VERSION = "v1"
API_PREFIX = f"/api/{API_VERSION}"

DOCUMENT_DIRECTORY = "backend/us_census"
VECTORSTORE_DIRECTORY = "backend/vectorstore"

SUPPORTED_DOCUMENT_TYPES = (".pdf",)

EMBEDDING_MODEL = "sentence-transformers/all-mpnet-base-v2"

LLM_REPOSITORY = "deepseek-ai/DeepSeek-R1-0528"
LLM_TASK = "text-generation"

LOG_FORMAT = (
    "%(asctime)s | "
    "%(levelname)s | "
    "%(name)s | "
    "%(filename)s:%(lineno)d | "
    "%(message)s"
)

LOG_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

APPLICATION_STARTED = "Application started."
CONFIGURATION_LOADED = "Configuration loaded successfully."
VECTORSTORE_CREATED = "Vector store created successfully."
NO_DOCUMENTS_FOUND = "No PDF documents found."
RAG_READY = "RAG pipeline initialized successfully."