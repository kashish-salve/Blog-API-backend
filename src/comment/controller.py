from src.comment.models import CommentModel
from src.utils.db import get_db
from sqlalchemy.orm import Session
from src.comment.dtos import CommentSchema
from src.user.models import UserModel
from src.blog.models import BlogModel
from fastapi import HTTPException


def create_comment(body:CommentSchema, blog_id: int, db: Session, user: UserModel):
    data = body.model_dump()
    new_comment = CommentModel(text=data["text"],user_id=user.id,blog_id=blog_id)

    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment


def get_comments(blog_id: int, db: Session):
    comments = db.query(CommentModel).filter(CommentModel.blog_id == blog_id).all()
    if not comments:
        return {"message": "No comments yet", "comments": []}
    return comments
    
    
def delete_comment(comment_id: int, db: Session, user: UserModel):
    comment = db.query(CommentModel).filter(CommentModel.id == comment_id).first()
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    if comment.user_id != user.id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this comment")
    
    db.delete(comment)
    db.commit()
    return {"message": "Comment deleted successfully"}    