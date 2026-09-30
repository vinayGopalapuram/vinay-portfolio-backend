from fastapi import APIRouter,Depends
from app.schemas.about import AboutResponse
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services.about import AboutService
from app.schemas.about import AboutCreate
from app.services.dependencies import get_current_admin


router=APIRouter(prefix="/about")

@router.get("",response_model=AboutResponse)
def get_about(db:Session=Depends(get_db)):
    service=AboutService(db)
    return service.get_about()


@router.post("",response_model=AboutResponse)
def create_about(about_data:AboutCreate,db:Session=Depends(get_db),admin:str=Depends(get_current_admin)):
    service=AboutService(db)
    return service.create_about(about_data)
