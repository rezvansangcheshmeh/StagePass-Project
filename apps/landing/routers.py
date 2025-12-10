# apps/landing/routers.py

from fastapi import APIRouter

router = APIRouter(tags=["Landing"])


@router.get("/")  # type:ignore [misc]
def root() -> dict[str, str]:
    return {"message": "Wellcome"}


@router.get("/about_us")  # type:ignore [misc]
def about_us() -> dict[str, str]:
    return {"message": "about_us"}
