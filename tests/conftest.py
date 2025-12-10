# tests/conftest.py
import pytest_asyncio
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from core.db.base import Base

TEST_DATABASE_URL = "sqlite+aiosqlite:///:memory:"

# Engine و Session مخصوص تست
engine = create_async_engine(TEST_DATABASE_URL, echo=False, future=True)
TestingSessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


@pytest_asyncio.fixture(scope="function")
async def session() -> AsyncSession:
    """هر تست یک دیتابیس ایزوله روی SQLite in-memory داشته باشد."""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    async with TestingSessionLocal() as session:
        yield session
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
