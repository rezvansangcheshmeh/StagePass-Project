from sqlalchemy.ext.asyncio import AsyncSession

from apps.accounts.users.models import User
from apps.accounts.users.repositories import UserRepository
from apps.accounts.users.schemas import UserCreate, UserUpdate
from core.security.password import hash_password, verify_password


class UserService:
    """Business logic for User operations."""

    @staticmethod
    async def register(session: AsyncSession, user_in: UserCreate) -> User:
        """ثبت‌نام کاربر جدید با هش کردن پسورد."""
        user_in.password = user_in.password
        return await UserRepository.create(session, user_in)

    @staticmethod
    async def authenticate(session: AsyncSession, email: str, password: str) -> User | None:
        """اعتبارسنجی کاربر با ایمیل و پسورد."""
        user = await UserRepository.get_by_email(session, email)
        if user and verify_password(password, user.hashed_password):
            return user
        return None

    @staticmethod
    async def get_by_id(session: AsyncSession, user_id: int) -> User | None:
        return await UserRepository.get_by_id(session, user_id)

    @staticmethod
    async def update_user(session: AsyncSession, user: User, user_in: UserUpdate) -> User:
        """آپدیت کاربر (با هش مجدد پسورد در صورت تغییر)."""
        if user_in.password:
            user_in.password = hash_password(user_in.password)
        return await UserRepository.update(session, user, user_in)

    @staticmethod
    async def delete_user(session: AsyncSession, user: User) -> None:
        await UserRepository.delete(session, user)
