from sqlalchemy.orm import Mapped,mapped_column
from app.db.base import Base
from sqlalchemy import String,Boolean

class User(Base):
    __tablename__="users"
    id:Mapped[int]=mapped_column(primary_key=True)
    username:Mapped[str]=mapped_column(String(150),nullable=False,unique=True)
    password_hash:Mapped[str]=mapped_column(String(300),nullable=False)
    is_admin:Mapped[bool]=mapped_column(Boolean,default=True,nullable=False)