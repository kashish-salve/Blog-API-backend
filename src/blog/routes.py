from fastapi import APIRouter ,Depends,HTTPException,status
from src.utils.helpers import is_authenticated
from src.user.models import UserModel
from src.blog.dtos import BlogSchema
from sqlalchemy.orm import Session
from src.utils.db import get_db
from src.blog import controller

blog_routes = APIRouter(prefix="/blog")

@blog_routes.post("/create",status_code=status.HTTP_201_CREATED)
def create_blog(body:BlogSchema,db:Session=Depends(get_db),user:UserModel=Depends(is_authenticated)):
    return controller.create_blog(body,db,user)

@blog_routes.get("/all_blogs",status_code=status.HTTP_200_OK)
def get_all_blogs(db:Session=Depends(get_db),user:UserModel=Depends(is_authenticated)):
    return controller.get_all_blogs(db,user)

@blog_routes.get("/one_blog/{blog_id}",status_code=status.HTTP_200_OK)
def get_blog_by_id(blog_id:int,db:Session=Depends(get_db),user:UserModel=Depends(is_authenticated)):
    return controller.get_blog_by_id(blog_id,db,user)

@blog_routes.put("/update_blog/{blog_id}",status_code=status.HTTP_201_CREATED)
def update_blog(body:BlogSchema,blog_id:int,db:Session=Depends(get_db),user:UserModel=Depends(is_authenticated)):
    return controller.update_blog(body,blog_id,db,user)


@blog_routes.delete("/delete_blog/{blog_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(blog_id:int,db:Session=Depends(get_db),user:UserModel=Depends(is_authenticated)):
    return controller.delete_blog(blog_id, db ,user)