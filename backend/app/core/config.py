"""
Application configuration.

This module centralizes all configurable values used by the RAGFlow AI
Platform. Settings are loaded from environment variables or the local
`.env` file using Pydantic Settings.
"""

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

from app.core.constants import (
    API_PREFIX,
    API_VERSION,
    APP_NAME,
    APP_VERSION,
    DOCUMENT_DIRECTORY,
    EMBEDDING_MODEL,
    LLM_REPOSITORY,
    LLM_TASK,
    LOG_DIRECTORY,
    VECTORSTORE_DIRECTORY,
)


class ProjectSettings(BaseModel):
    """General project information."""

    name: str = APP_NAME
    version: str = APP_VERSION
    environment: str = "development"


class APISettings(BaseModel):
    """REST API configuration."""

    version: str = API_VERSION
    prefix: str = API_PREFIX


class HuggingFaceSettings(BaseModel):
    """Hugging Face Hub configuration."""

    api_token: str
    provider: str = "auto"


class EmbeddingSettings(BaseModel):
    """Embedding model configuration."""

    model_name: str = EMBEDDING_MODEL
    device: str = "cpu"
    normalize_embeddings: bool = False


class DocumentSettings(BaseModel):
    """Configuration for document loading and chunking."""

    pdf_directory: str = DOCUMENT_DIRECTORY
    chunk_size: int = 1000
    chunk_overlap: int = 200


class VectorStoreSettings(BaseModel):
    """Vector store configuration."""

    directory: str = VECTORSTORE_DIRECTORY


class LLMSettings(BaseModel):
    """Large language model configuration."""

    repository: str = LLM_REPOSITORY
    task: str = LLM_TASK
    max_new_tokens: int = 512
    temperature: float = 0.0
    repetition_penalty: float = 1.03


class LoggingSettings(BaseModel):
    """Application logging configuration."""

    level: str = "INFO"
    directory: str = LOG_DIRECTORY


class AppSettings(BaseSettings):
    """Application settings loaded from the environment."""

    HUGGINGFACEHUB_API_TOKEN: str

    project: ProjectSettings = ProjectSettings()
    api: APISettings = APISettings()
    embedding: EmbeddingSettings = EmbeddingSettings()
    document: DocumentSettings = DocumentSettings()
    vectorstore: VectorStoreSettings = VectorStoreSettings()
    llm: LLMSettings = LLMSettings()
    logging: LoggingSettings = LoggingSettings()

    @property
    def huggingface(self) -> HuggingFaceSettings:
        """
        Return the Hugging Face configuration.
        The API token is loaded directly from the environment while the
        remaining Hugging Face settings use application defaults.
        """

        return HuggingFaceSettings(
            api_token=self.HUGGINGFACEHUB_API_TOKEN,
        )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = AppSettings()