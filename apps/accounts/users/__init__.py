# apps/accounts/users/__init__.py

from .models import User
from .routers import router as user_router

__all__: list[str] = ["User", 'user_router']
