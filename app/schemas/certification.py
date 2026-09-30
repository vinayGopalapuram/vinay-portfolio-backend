from pydantic import BaseModel,ConfigDict,Field

class CertificationResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str
    issuer: str
    issue_date: str
    credential_url: str | None
    description: str | None


class CertificationCreate(BaseModel):
    name: str=Field(min_length=2,max_length=100)
    issuer: str=Field(min_length=2,max_length=100)
    issue_date: str=Field(min_length=4,max_length=50)
    credential_url: str | None=None
    description: str | None=None