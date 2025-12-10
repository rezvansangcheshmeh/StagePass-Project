# core/db/deps.py
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from core.db.session import SessionLocal


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    """FastAPI dependency برای Postgres در اپ اصلی."""
    async with SessionLocal() as session:
        yield session
