from pydantic import BaseModel,ConfigDict,HttpUrl,Field

class ProjectListResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    project_name: str
    github_url: str
    description: str


class ProjectDetailResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    project_name: str
    github_url: str
    description: str
    tech_stack: list[str]
    architecture: str
    challenges: str
    results: str

class ProjectCreate(BaseModel):
    project_name: str=Field(min_length=2,max_length=100)
    github_url: HttpUrl
    description: str=Field(min_length=2,max_length=2000)
    tech_stack: list[str]=Field(min_length=1)
    architecture: str=Field(min_length=2,max_length=1000)
    challenges: str=Field(min_length=2,max_length=1000)
    results: str=Field(min_length=2,max_length=1000)