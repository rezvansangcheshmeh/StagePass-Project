# core/db/session.py
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from core.config.settings import get_settings

settings = get_settings()

# -------------------------
# Main Application Database (Postgres)
# -------------------------
engine = create_async_engine(
    settings.postgres_url,  # همیشه Postgres برای اپ
    echo=settings.debug,
    future=True,
)

SessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

# -------------------------
# Testing Database (SQLite in-memory)
# -------------------------
test_engine = create_async_engine(
    settings.test_database_url,
    echo=False,
    future=True,
)

TestingSessionLocal = sessionmaker(
    bind=test_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)
