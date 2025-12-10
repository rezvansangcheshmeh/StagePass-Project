# api/main.py

from fastapi import FastAPI

from apps import router_list
from core.config.settings import get_settings

settings = get_settings()

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description=settings.APP_DESCRIPTION,
    debug=settings.DEBUG,
)

for router in router_list:
    app.include_router(router)
