from app.models.skills import Skill
from app.schemas.skills import SkillCreate
from sqlalchemy import select
from sqlalchemy.orm import Session
from fastapi import HTTPException

class SkillService:
    def __init__(self,db:Session):
        self.db =db

    def get_all_skills(self)->list[Skill]:
        stmt=select(Skill).order_by(Skill.category,Skill.name)
        return self.db.scalars(stmt).all()

    def create_skills(self,skill_data:SkillCreate)-> Skill:
        stmt=select(Skill).where(Skill.name==skill_data.name,Skill.category==skill_data.category)

        existing_skill=self.db.scalars(stmt).first()

        if existing_skill is not None:
            raise HTTPException(
                status_code=409,detail="Skill already exists" 
            )

        skill=Skill(name=skill_data.name,category=skill_data.category)
        self.db.add(skill)
        self.db.commit()
        self.db.refresh(skill)

        return skill