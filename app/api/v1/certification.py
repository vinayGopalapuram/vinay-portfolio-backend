from fastapi import APIRouter,Depends
from app.schemas.certification import CertificationResponse,CertificationCreate
from app.db.session import get_db
from sqlalchemy.orm import Session
from app.services.certification import CertificationService
from app.services.dependencies import get_current_admin

router=APIRouter(prefix="/certifications")

@router.get("",response_model=list[CertificationResponse])
def get_certification(db:Session = Depends(get_db)):
    service=CertificationService(db)
    return service.get_all_certifications()

@router.post("",response_model=CertificationResponse)
def create_certification(certification_data:CertificationCreate,db:Session=Depends(get_db),admmin:str=Depends(get_current_admin)):
    service=CertificationService(db)
    return service.create_certification(certification_data)
