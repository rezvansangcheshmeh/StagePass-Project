# core/security/dependencies.py
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from core.security.jwt import decode_token

# tokenUrl باید به endpoint واقعی لاگین اشاره کند (بعداً در apps/accounts/auth/routers.py)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/accounts/auth/login")


def get_current_user(token: str = Depends(oauth2_scheme)) -> dict[str, str]:
    try:
        payload = decode_token(token)
        user_id = payload.get("sub")
        if not user_id:
            raise ValueError("Token missing subject")
        return {"id": user_id}
    except Exception as err:  # Add 'as err'
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
        ) from err  # Chain original exception
