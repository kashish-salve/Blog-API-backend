from sqlalchemy import Column,Integer,String,Boolean
from src.utils.db import Base
from sqlalchemy.orm import relationship


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer,primary_key=True)
    name = Column(String,nullable=False)
    username = Column(String,nullable=False)
    hash_password = Column(String,nullable=False)
    email = Column(String)

    blogs = relationship("BlogModel", back_populates="user")