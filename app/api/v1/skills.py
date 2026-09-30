from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.skills import SkillCreate, SkillResponse
from app.services.dependencies import get_current_admin
from app.services.skills import SkillService


router = APIRouter(prefix="/skills",tags=["Skills"])


@router.get("",response_model=list[SkillResponse])
def get_skills(db: Session = Depends(get_db)):
    service = SkillService(db)
    return service.get_all_skills()


@router.post("",response_model=SkillResponse)
def create_skill(skill_data: SkillCreate,db: Session = Depends(get_db),admin: str = Depends(get_current_admin)):
    service = SkillService(db)
    return service.create_skills(skill_data)