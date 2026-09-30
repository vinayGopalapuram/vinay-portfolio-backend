from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import String, Text
from app.db.base import Base


class Education(Base):
    __tablename__="education"
    id:Mapped[int]=mapped_column(primary_key=True)
    level:Mapped[str]=mapped_column(String(50),nullable=False)
    institution:Mapped[str]=mapped_column(String(200),nullable=False)
    field_of_study:Mapped[str | None]=mapped_column(String(150),nullable=True)
    location:Mapped[str]=mapped_column(String(100),nullable=False)
    start_year:Mapped[int]=mapped_column(nullable=False)
    end_year:Mapped[int]=mapped_column(nullable=False)



