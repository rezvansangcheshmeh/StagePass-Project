# core/config/settings.py
from functools import lru_cache
from urllib.parse import quote_plus

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):  # type:ignore [misc]
    """Application settings loaded from environment variables."""

    # =========================
    # APP CONFIGURATION
    # =========================
    APP_NAME: str = "StagePass"
    APP_VERSION: str = "0.0.0"
    APP_DESCRIPTION: str = "Unified Environment"
    DEBUG: bool = True

    # =========================
    # DATABASE CONFIGURATION
    # =========================
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    DB_HOST: str = "localhost"  # در لوکال localhost، در Docker مقدارش postgres میشه
    DB_PORT: int = 5432

    DATABASE_URL: str | None = None
    TEST_DATABASE_URL: str = "sqlite+aiosqlite:///:memory:"

    # =========================
    # SECURITY CONFIGURATION
    # =========================
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    ALGORITHM: str = "HS256"

    # =========================
    # MODEL CONFIGURATION
    # =========================
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_prefix="",  # exact match to .env keys
        extra="ignore",
    )

    # =========================
    # HELPER PROPERTIES
    # =========================
    @property
    def postgres_url(self) -> str:
        """Async URL برای اپ اصلی (FastAPI)."""
        if self.DATABASE_URL:
            return self.DATABASE_URL
        pwd = quote_plus(self.DB_PASSWORD)
        return f"postgresql+asyncpg://{self.DB_USER}:{pwd}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def postgres_url_sync(self) -> str:
        """Sync URL برای Alembic migrations."""
        if self.DATABASE_URL:
            return self.DATABASE_URL.replace("asyncpg", "psycopg")
        pwd = quote_plus(self.DB_PASSWORD)
        return f"postgresql+psycopg://{self.DB_USER}:{pwd}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


@lru_cache
def get_settings() -> Settings:
    """Return a cached Settings instance (singleton)."""
    return Settings()
