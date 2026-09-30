from pydantic import BaseModel, ConfigDict,Field

class SkillResponse(BaseModel):
    model_config=ConfigDict(from_attributes=True)
    name:str
    category:str

class SkillCreate(BaseModel):
    name:str=Field(min_length=2,max_length=100)
    category:str=Field(min_length=2,max_length=100)
    