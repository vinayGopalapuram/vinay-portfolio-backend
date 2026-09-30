from pydantic import BaseModel,ConfigDict,Field,model_validator

class EducationResponse(BaseModel):
    model_config=ConfigDict(from_attributes=True)
    level:str
    institution: str
    field_of_study: str | None
    location: str
    start_year: int
    end_year: int

class EducationCreate(BaseModel):
    level: str=Field(min_length=2,max_length=50)
    institution: str=Field(min_length=2,max_length=200)
    field_of_study: str | None = Field(default=None,max_length=150)
    location: str=Field(min_length=2,max_length=200)
    start_year: int=Field(ge=1950,le=2100)
    end_year: int=Field(ge=1950,le=2100)

    # this is to give the user an exception if the start year is grater than end year 
    @model_validator(mode="after")
    def validate_years(self):
        if self.start_year > self.end_year:
            raise ValueError("start_year cannot be after end_year")

        return self