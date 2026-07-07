"""
Application-wide constant values.

Constants defined here remain unchanged during runtime and are shared
across different modules of the application.
"""

# ============================================================================
# Project
# ============================================================================

APP_NAME = "RAGFlow AI Platform"
APP_VERSION = "1.0.0"

# ============================================================================
# API
# ============================================================================

API_VERSION = "v1"
API_PREFIX = f"/api/{API_VERSION}"

# ============================================================================
# Documents
# ============================================================================

DOCUMENT_DIRECTORY = "backend/us_census"

SUPPORTED_DOCUMENT_TYPES = (
    ".pdf",
)

# ============================================================================
# Vector Store
# ============================================================================

VECTORSTORE_DIRECTORY = "backend/vectorstore"

# ============================================================================
# Embedding Model
# ============================================================================

EMBEDDING_MODEL = "sentence-transformers/all-mpnet-base-v2"

# ============================================================================
# Large Language Model
# ============================================================================

LLM_REPOSITORY = "deepseek-ai/DeepSeek-R1-0528"
LLM_TASK = "text-generation"

# ============================================================================
# Retrieval
# ============================================================================

DEFAULT_TOP_K = 4
DEFAULT_SEARCH_TYPE = "similarity"

# ============================================================================
# Logging
# ============================================================================

LOG_FORMAT = (
    "%(asctime)s | "
    "%(levelname)s | "
    "%(name)s | "
    "%(filename)s:%(lineno)d | "
    "%(message)s"
)

LOG_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

LOG_DIRECTORY = "logs"

# ============================================================================
# Application Messages
# ============================================================================

# APPLICATION_STARTED = "Application started."
# CONFIGURATION_LOADED = "Configuration loaded successfully."
# VECTORSTORE_CREATED = "Vector store created successfully."
# NO_DOCUMENTS_FOUND = "No PDF documents found."
# RAG_READY = "RAG pipeline initialized successfully."