from app.models.project import Project
from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.schemas.projects import ProjectCreate



class ProjectService:

    def __init__(self,db:Session):
        self.db=db

    def get_all_projects(self) -> list[Project]:
        stmt=select(Project)
        return self.db.scalars(stmt).all()

    def get_project(self, project_name: str) -> Project:
        stmt=select(Project).where(Project.project_name== project_name)
        project = self.db.scalars(stmt).first()

        if project is None:
            raise HTTPException(status_code=404,detail="Project Not Found")

        return project

    def create_project(self,project_data:ProjectCreate):
        project=Project(
            project_name=project_data.project_name,
            github_url=str(project_data.github_url),
            description=project_data.description,
            tech_stack=project_data.tech_stack,
            architecture=project_data.architecture,
            challenges=project_data.challenges,
            results=project_data.results
        )

        self.db.add(project)
        self.db.commit()
        self.db.refresh(project)

        return project