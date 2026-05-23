from src.utils.db import get_db
from sqlalchemy.orm import Session
from src.like.models import LikeModel
from src.user.models import UserModel
from src.blog.models import BlogModel
from fastapi import HTTPException

def create_like(blog_id: int, db: Session, user: UserModel):
    blog = db.query(BlogModel).filter(BlogModel.id == blog_id).first()
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    
    existing_like = db.query(LikeModel).filter(LikeModel.blog_id == blog_id, LikeModel.user_id == user.id).first()
    if existing_like:
        raise HTTPException(status_code=400, detail="You have already liked this blog")
    
    new_like = LikeModel(user_id=user.id, blog_id=blog_id)
    db.add(new_like)
    db.commit()
    db.refresh(new_like)
    return new_like

def unlike_blog(blog_id: int, db: Session, user: UserModel):
    like = db.query(LikeModel).filter(LikeModel.blog_id == blog_id, LikeModel.user_id == user.id).first()
    if not like:
        raise HTTPException(status_code=404, detail="Like not found")
    
    db.delete(like)
    db.commit()
    return {"detail": "Blog unliked successfully"}