import pytest

from apps.accounts.users.repositories import UserRepository
from apps.accounts.users.schemas import UserCreate, UserUpdate
from apps.accounts.users.services import UserService


@pytest.mark.asyncio
async def test_create_user(session):
    user_in = UserCreate(email="test@example.com", username="testuser", password="secret123")
    user = await UserService.register(session, user_in)
    assert user.id is not None
    assert user.email == "test@example.com"
    assert user.username == "testuser"
    assert user.hashed_password != "secret123"  # پسورد باید هش شده باشد


@pytest.mark.asyncio
async def test_get_user_by_email(session):
    user_in = UserCreate(email="findme@example.com", username="findme", password="secret123")
    await UserService.register(session, user_in)

    user = await UserRepository.get_by_email(session, "findme@example.com")
    assert user is not None
    assert user.username == "findme"


@pytest.mark.asyncio
async def test_update_user(session):
    user_in = UserCreate(email="update@example.com", username="updatable", password="secret123")
    user = await UserService.register(session, user_in)

    update_in = UserUpdate(username="updated")
    updated_user = await UserService.update_user(session, user, update_in)
    assert updated_user.username == "updated"


@pytest.mark.asyncio
async def test_delete_user(session):
    user_in = UserCreate(email="delete@example.com", username="deleteme", password="secret123")
    user = await UserService.register(session, user_in)

    await UserService.delete_user(session, user)
    deleted = await UserRepository.get_by_email(session, "delete@example.com")
    assert deleted is None


@pytest.mark.asyncio
async def test_authenticate_user(session):
    user_in = UserCreate(email="auth@example.com", username="authuser", password="secret123")
    await UserService.register(session, user_in)

    user = await UserService.authenticate(session, "auth@example.com", "secret123")
    assert user is not None

    wrong = await UserService.authenticate(session, "auth@example.com", "wrongpass")
    assert wrong is None
