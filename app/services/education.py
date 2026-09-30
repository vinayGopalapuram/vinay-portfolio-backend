from app.models.education import Education
from app.schemas.education import EducationCreate
from sqlalchemy import select
from sqlalchemy.orm import Session

class EducationService:
    def __init__(self,db:Session):
        self.db=db

    def get_education(self)->list[Education]:
        stmt=select(Education).order_by(Education.end_year.desc())
        return self.db.scalars(stmt).all()

    def create_education(self,edu_data:EducationCreate)->Education:
        education=Education(
            level=edu_data.level,
            institution=edu_data.institution,
            field_of_study=edu_data.field_of_study,
            location=edu_data.location,
            start_year=edu_data.start_year,
            end_year=edu_data.end_year
        )
        self.db.add(education)
        self.db.commit()
        self.db.refresh(education)

        return education