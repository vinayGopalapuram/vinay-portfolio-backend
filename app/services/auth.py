import bcrypt
from fastapi import HTTPException
from app.models.user import User
from app.schemas.auth import Loginreq
from sqlalchemy.orm import Session
from sqlalchemy import select
import os
from dotenv import load_dotenv
from datetime import datetime,timedelta,timezone
import jwt

load_dotenv()

def hash_password(password: str) -> str:
    password_bytes = password.encode("utf-8")
    hashed_password = bcrypt.hashpw(password_bytes,bcrypt.gensalt(),)
    return hashed_password.decode("utf-8")

def verify_password(password: str, password_hash: str) -> bool:
    password_bytes = password.encode("utf-8")
    hash_bytes = password_hash.encode("utf-8")
    return bcrypt.checkpw(password_bytes,hash_bytes,)

def authenticate_user(db:Session,login_data:Loginreq):
    stmt=select(User).where(User.username==login_data.username)
    user=db.scalars(stmt).first()

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )
    if not verify_password(login_data.password,user.password_hash):
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )
    if not user.is_admin:
        raise HTTPException(
            status_code=403,
            detail="Admin access required",
        )
    return user

JWT_SECRET= os.getenv("JWT_SECRET")

if not JWT_SECRET:
    raise RuntimeError("JWT_SECRET IS NOT SET")

JWT_ALGORITHM ="HS256"
JWT_EXPIRE_MINUTES=60


def create_access_token(user:User):
    expire=datetime.now(timezone.utc)+timedelta(minutes=JWT_EXPIRE_MINUTES)
    payload={
        "sub": user.username,
        "is_admin": user.is_admin,
        "exp": expire
    }
    token = jwt.encode(
        payload,
        JWT_SECRET,
        algorithm=JWT_ALGORITHM,
    )

    return token
