from sqlalchemy.orm import mapped_column,Mapped
from app.db.base import Base
from sqlalchemy import String,Text

class About(Base):
    __tablename__="about_me"
    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]=mapped_column(String(150),nullable=False)
    headline:Mapped[str]=mapped_column(String(200),nullable=False)
    bio: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    location: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    email: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    github_url: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
    )

    linkedin_url: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
    )
    