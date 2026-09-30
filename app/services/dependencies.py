from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
import jwt
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services.auth import JWT_ALGORITHM, JWT_SECRET
from app.services.projects import ProjectService


def get_project_service(db: Session = Depends(get_db)) -> ProjectService:
    return ProjectService(db)


security = HTTPBearer()


def get_current_admin(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials

    try:
        payload = jwt.decode(
            token,
            JWT_SECRET,
            algorithms=[JWT_ALGORITHM],
        )

    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=401,
            detail="Token has expired",
        )

    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=401,
            detail="Invalid token",
        )

    username = payload.get("sub")
    is_admin = payload.get("is_admin")

    if not username:
        raise HTTPException(
            status_code=401,
            detail="Invalid token",
        )

    if is_admin is not True:
        raise HTTPException(
            status_code=403,
            detail="Admin access required",
        )

    return username