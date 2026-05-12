from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship
from src.utils.db import Base


class BlogModel(Base):
    __tablename__ = "blogs"

    id = Column(Integer,primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String,nullable=False)
    user_id =Column(Integer,ForeignKey("users.id"))

    user = relationship("UserModel", back_populates="blogs")


    
