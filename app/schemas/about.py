from pydantic import BaseModel, ConfigDict, HttpUrl


class AboutResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str
    headline: str
    bio: str
    location: str
    email: str
    github_url: HttpUrl
    linkedin_url: HttpUrl


class AboutCreate(BaseModel):
    name: str
    headline: str
    bio: str
    location: str
    email: str
    github_url: HttpUrl
    linkedin_url: HttpUrl