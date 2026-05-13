from fastapi import APIRouter, HTTPException,Depends
from sqlalchemy.orm import Session
from src.comment import controller
from src.comment.dtos import CommentSchema
from src.utils.db import get_db
from src.user.models import UserModel
from src.utils.helpers import is_authenticated


comment_routes = APIRouter(prefix="/comments")

@comment_routes.post("/ blog/{blog_id}")
def add_comment(blog_id: int, body: CommentSchema, db: Session = Depends(get_db),user: UserModel = Depends(is_authenticated)):
    return controller. create_comment(body, blog_id, db, user)


@comment_routes.get("/blog/{blog_id}")
def get_comments(blog_id: int, db: Session = Depends(get_db)):
    return controller.get_comments(blog_id,db)


@comment_routes.delete("/{comment_id}")
def delete_comment(comment_id: int, db: Session = Depends(get_db), user: UserModel = Depends(is_authenticated)):
    return controller.delete_comment(comment_id, db, user)