from fastapi import FastAPI
from app.api.v1.projects import router as projects_router
from app.api.v1.auth import router as auth_router
from app.api.v1.about import router as about_router
from app.api.v1.skills import router as skill_router
from app.api.v1.education import router as education_router
from app.api.v1.certification import router as certification_router
from app.core.exceptions import general_exception_handler,integrity_error_handler
from sqlalchemy.exc import IntegrityError

from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

app.include_router(projects_router,prefix="/api/v1")

app.include_router(auth_router,prefix="/api/v1")

app.include_router(about_router,prefix="/api/v1")

app.include_router(skill_router,prefix="/api/v1")

app.include_router(education_router,prefix="/api/v1")

app.include_router(certification_router,prefix="/api/v1")

app.add_exception_handler(IntegrityError,integrity_error_handler)

app.add_exception_handler(Exception,general_exception_handler)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173","https://vinay-portfolio-lovat.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/v1/health")
def health_check():
    return {"status": "healthy"}
