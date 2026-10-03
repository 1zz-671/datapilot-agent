from functools import lru_cache
from typing import Literal

from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_prefix="DATAPILOT_",
        extra="forbid",
    )

    app_name: str = "DataPilot API"
    environment: Literal["local", "test", "production"] = "local"
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR"] = "INFO"

    database_url: SecretStr | None = None

    query_max_rows: int = Field(default=200, ge=1, le=1000)
    query_timeout_seconds: int = Field(default=10, ge=1, le=60)


@lru_cache
def get_settings() -> Settings:
    return Settings()