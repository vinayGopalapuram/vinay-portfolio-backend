from fastapi import APIRouter,Depends
from app.db.session import get_db
from app.schemas.auth import Loginreq
from sqlalchemy.orm import Session
from app.services.auth import authenticate_user,create_access_token

router=APIRouter(prefix="/auth")

@router.post("/login")
def login(
    Login_data:Loginreq,
    db:Session=Depends(get_db)
):
    user=authenticate_user(db,Login_data)

    access_token=create_access_token(user)

    return{
        "access_token": access_token,
        "token_type":"bearer"
    }