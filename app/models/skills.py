from sqlalchemy import String,UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base

class Skill(Base):
    __tablename__ = "skills"

    __table_args__=(
        UniqueConstraint("name","category",name="uq_skill"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100),nullable=False)
    category: Mapped[str] = mapped_column(String(100),nullable=False)