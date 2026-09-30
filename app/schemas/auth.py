from pydantic import BaseModel

class Loginreq(BaseModel):
    username:str
    password:str