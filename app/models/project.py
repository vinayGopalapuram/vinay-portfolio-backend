from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import String, Text
from app.db.base import Base
from sqlalchemy.dialects.postgresql import ARRAY


class Project(Base):
    __tablename__="projects"

    id:Mapped[int]=mapped_column(primary_key=True)
    project_name:Mapped[str]=mapped_column(String(150),nullable=False)
    github_url:Mapped[str]=mapped_column(String(500),nullable=False)
    description:Mapped[str]=mapped_column(Text,nullable=False)
    tech_stack:Mapped[list[str]]=mapped_column(ARRAY(String),nullable=False,)
    architecture:Mapped[str]=mapped_column(Text,nullable=False)
    challenges:Mapped[str]=mapped_column(Text,nullable=False)
    results:Mapped[str]=mapped_column(Text,nullable=False)
