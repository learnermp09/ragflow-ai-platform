"""
Application configuration.

This module centralizes all configurable values used by the RAGFlow AI
Platform. Settings are loaded from environment variables or the local
`.env` file using Pydantic Settings.
"""

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class ProjectSettings(BaseModel):
    """General project information."""

    name: str = "RAGFlow AI Platform"
    version: str = "1.0.0"
    environment: str = "development"


class HuggingFaceSettings(BaseModel):
    """Hugging Face Hub configuration."""

    api_token: str
    provider: str = "auto"


class EmbeddingSettings(BaseModel):
    """Embedding model configuration."""

    model_name: str = "sentence-transformers/all-mpnet-base-v2"
    device: str = "cpu"
    normalize_embeddings: bool = False


class DocumentSettings(BaseModel):
    """Configuration for document loading and chunking."""

    pdf_directory: str = "backend/us_census"
    chunk_size: int = 1000
    chunk_overlap: int = 200


class VectorStoreSettings(BaseModel):
    """Vector store configuration."""

    directory: str = "backend/vectorstore"


class LLMSettings(BaseModel):
    """Large language model configuration."""

    repository: str = "deepseek-ai/DeepSeek-R1-0528"
    task: str = "text-generation"
    max_new_tokens: int = 512
    temperature: float = 0.0
    repetition_penalty: float = 1.03


class LoggingSettings(BaseModel):
    """Application logging configuration."""

    level: str = "INFO"
    directory: str = "logs"


class AppSettings(BaseSettings):
    """Application settings loaded from the environment."""

    HUGGINGFACEHUB_API_TOKEN: str

    project: ProjectSettings = ProjectSettings()
    embedding: EmbeddingSettings = EmbeddingSettings()
    document: DocumentSettings = DocumentSettings()
    vectorstore: VectorStoreSettings = VectorStoreSettings()
    llm: LLMSettings = LLMSettings()
    logging: LoggingSettings = LoggingSettings()

    @property
    def huggingface(self) -> HuggingFaceSettings:
        """Return the Hugging Face configuration."""

        return HuggingFaceSettings(
            api_token=self.HUGGINGFACEHUB_API_TOKEN,
        )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = AppSettings()