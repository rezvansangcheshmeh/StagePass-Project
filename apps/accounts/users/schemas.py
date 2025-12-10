# app/schemas/user.py
from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr


class UserBase(BaseModel):
    """Shared fields between input/output schemas."""

    email: EmailStr
    username: str
    is_active: bool = True
    is_superuser: bool = False


class UserCreate(UserBase):
    """Schema for creating a new user (input)."""

    password: str


class UserUpdate(BaseModel):
    """Schema for updating user fields (partial update)."""

    email: Optional[EmailStr] = None
    username: Optional[str] = None
    password: Optional[str] = None
    is_active: Optional[bool] = None
    is_superuser: Optional[bool] = None


class UserRead(UserBase):
    """Schema for reading user data (output)."""

    id: int

    model_config = ConfigDict(from_attributes=True)
