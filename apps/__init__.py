# apps/__init__.py

from fastapi.routing import APIRouter

from .accounts.users import User, user_router
from .landing import landing_router

router_list: list[APIRouter] = [
    landing_router,
    user_router,
]
model_list = [User]
