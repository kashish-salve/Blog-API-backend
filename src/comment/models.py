from sqlalchemy import Column,Integer, String,ForeignKey
from sqlalchemy.orm import relationship
from src.utils.db import Base

class CommentModel(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True,)
    text = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    blog_id = Column(Integer, ForeignKey("blogs.id"))

    user = relationship("UserModel", back_populates="comments")
    blog = relationship("BlogModel", back_populates="comments")