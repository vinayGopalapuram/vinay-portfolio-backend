from fastapi import APIRouter,Depends
from app.schemas.education import EducationResponse,EducationCreate
from app.db.session import get_db
from sqlalchemy.orm import Session
from app.services.education import EducationService
from app.services.dependencies import get_current_admin

router=APIRouter(prefix="/education")

@router.get("",response_model=list[EducationResponse])
def get_education(db:Session = Depends(get_db)):
    service=EducationService(db)
    return service.get_education()

@router.post("",response_model=EducationResponse)
def create_education(education_data:EducationCreate,
                     db:Session = Depends(get_db),admin:str=Depends(get_current_admin)):
    service=EducationService(db)
    return service.create_education(education_data)

list[EducationResponse]