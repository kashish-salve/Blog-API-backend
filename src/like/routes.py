from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.like import controller
from src.utils.db import get_db
from src.user.models import UserModel
from src.utils.helpers import is_authenticated

like_routes = APIRouter(prefix="/likes")

@like_routes.post("/blog/{blog_id}")
def like_blog(blog_id: int, db: Session = Depends(get_db), user: UserModel = Depends(is_authenticated)):
    return controller.create_like(blog_id, db, user)


@like_routes.delete("/blog/{blog_id}")
def remove_like(blog_id: int, db: Session = Depends(get_db), user: UserModel = Depends(is_authenticated)):
    return controller.unlike_blog(blog_id, db, user)