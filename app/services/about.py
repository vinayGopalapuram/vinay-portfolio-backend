from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.aboutme import About
from app.schemas.about import AboutCreate

class AboutService:
    def __init__(self,db:Session):
        self.db = db

    def get_about(self) -> About:
        stmt =select(About)
        about=self.db.scalars(stmt).first()
        if about is None:
            raise HTTPException(
                status_code=404,
                detail="About info not found"
            )
        return about

    def create_about(self, about_data: AboutCreate) -> About:
        existing_about = self.db.scalars(
            select(About)
        ).first()

        if existing_about is not None:
            raise HTTPException(
                status_code=409,
                detail="About information already exists",
            )

        about = About(
            name=about_data.name,
            headline=about_data.headline,
            bio=about_data.bio,
            location=about_data.location,
            email=about_data.email,
            github_url=str(about_data.github_url),
            linkedin_url=str(about_data.linkedin_url),
        )

        self.db.add(about)
        self.db.commit()
        self.db.refresh(about)

        return about
        
        