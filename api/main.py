# api/main.py

from fastapi import FastAPI

from apps import router_list

app = FastAPI()

for router in router_list:
    app.include_router(router)
