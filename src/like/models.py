from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.utils.db import Base


class LikeModel(Base):
    __tablename__ = "likes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    blog_id = Column(Integer, ForeignKey("blogs.id"))

    user = relationship("UserModel", back_populates="likes")
    blog = relationship("BlogModel", back_populates="likes")