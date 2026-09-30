from fastapi import APIRouter,Depends
from app.services.projects import ProjectService
from app.services.dependencies import get_project_service,get_current_admin
from sqlalchemy.orm import Session
from app.schemas.projects import ProjectListResponse,ProjectDetailResponse,ProjectCreate

router=APIRouter(prefix="/projects")

@router.get("", response_model=list[ProjectListResponse])
def get_projects(services:ProjectService=Depends(get_project_service),):
    return services.get_all_projects()

@router.get("/{project_name}",response_model=ProjectDetailResponse,)
def get_project(project_name: str,services: ProjectService = Depends(get_project_service),):
    return services.get_project(project_name)

@router.post("",response_model=ProjectDetailResponse)
def create_project(project_data:ProjectCreate,services:ProjectService=Depends(get_project_service),admin:str=Depends(get_current_admin)):
    return services.create_project(project_data)