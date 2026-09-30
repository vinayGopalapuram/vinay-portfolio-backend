from sqlalchemy import select,String,Text
from sqlalchemy.orm import mapped_column,Mapped
from app.db.base import Base

class Certification(Base):
    __tablename__="certification"
    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]=mapped_column(String(200),nullable=False)
    issuer:Mapped[str]=mapped_column(String(150),nullable= False)
    issue_date:Mapped[str]=mapped_column(String(150),nullable= False)
    credential_url:Mapped[str | None]=mapped_column(String(500),nullable= True)
    description:Mapped[str | None]=mapped_column(Text,nullable=True)
    