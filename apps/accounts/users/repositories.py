# apps/accounts/users/repositories.py

from typing import List, Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from apps.accounts.users.models import User
from apps.accounts.users.schemas import UserCreate, UserUpdate
from core.security.password import hash_password


class UserRepository:
    """Repository layer for User model."""

    @staticmethod
    async def create(session: AsyncSession, user_in: UserCreate) -> User:
        user = User(
            email=user_in.email,
            username=user_in.username,
            hashed_password=hash_password(user_in.password),
            is_active=user_in.is_active,
            is_superuser=user_in.is_superuser,
            role="admin" if getattr(user_in, "is_superuser", False) else "user",  # noqa
        )
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return user

    @staticmethod
    async def get_by_id(session: AsyncSession, user_id: int) -> Optional[User]:
        result = await session.execute(select(User).where(User.id == user_id))
        return result.scalar_one_or_none()

    @staticmethod
    async def get_by_email(session: AsyncSession, email: str) -> Optional[User]:
        result = await session.execute(select(User).where(User.email == email))
        return result.scalar_one_or_none()

    @staticmethod
    async def list(session: AsyncSession, skip: int = 0, limit: int = 100) -> List[User]:
        result = await session.execute(select(User).offset(skip).limit(limit))
        return result.scalars().all()

    @staticmethod
    async def update(session: AsyncSession, user: User, user_in: UserUpdate) -> User:
        for field, value in user_in.dict(exclude_unset=True).items():
            setattr(user, field, value)
        await session.commit()
        await session.refresh(user)
        return user

    @staticmethod
    async def delete(session: AsyncSession, user: User) -> None:
        await session.delete(user)
        await session.commit()
