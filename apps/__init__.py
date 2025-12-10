# apps/__init__.py

from fastapi.routing import APIRouter

from .landing import landing_router

router_list: list[APIRouter] = [landing_router]
# model_list = []
