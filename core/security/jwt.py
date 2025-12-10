# core/security/jwt.py
from datetime import datetime, timedelta, timezone
from typing import Any, Dict

import jwt

from core.config.settings import settings


def create_access_token(
    sub: str, minutes: int | None = None, extra: Dict[str, Any] | None = None
) -> str:
    exp_minutes = minutes or settings.token_exp_minutes
    now = datetime.now(timezone.utc)

    payload: Dict[str, Any] = {
        "sub": sub,
        "iat": int(now.timestamp()),
        "exp": int((now + timedelta(minutes=exp_minutes)).timestamp()),
    }
    if extra:
        payload.update(extra)

    return jwt.encode(payload, settings.jwt_secret, algorithm=settings.jwt_algorithm)


def decode_token(token: str) -> Dict[str, Any]:
    return jwt.decode(token, settings.jwt_secret, algorithms=[settings.jwt_algorithm])
