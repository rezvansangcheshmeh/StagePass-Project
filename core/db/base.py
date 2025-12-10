# core/db/base.py
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Global SQLAlchemy declarative base for all ORM models."""

    pass
