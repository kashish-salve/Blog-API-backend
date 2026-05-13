from sqlalchemy.orm import Session
from src.utils.db import get_db
from src.blog.dtos import BlogSchema
from src.blog.models import BlogModel
from src.user.models import UserModel
from fastapi import HTTPException



def create_blog(body:BlogSchema,db:Session,user:UserModel):
    data = body.model_dump()
    new_blog = BlogModel(title=data["title"],content=data["content"],user_id=user.id)

    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def get_all_blogs(db:Session,user:UserModel):
    blogs = db.query(BlogModel).filter(BlogModel.user_id == user.id).all()
    return blogs
    

def get_blog_by_id(blog_id:int,db:Session,user:UserModel):
    one_blog = db.query(BlogModel).get(blog_id)
    if not one_blog:
        raise HTTPException(404,detail="blog id is incorrect")
    return one_blog

def update_blog(body:BlogSchema,blog_id:int,db:Session,user:UserModel):
    one_blog:BlogModel = db.query(BlogModel).get(blog_id)
    if not one_blog:
        raise HTTPException(404,detail="blog id is incorrect")
    if one_blog.user_id != user.id:
        raise HTTPException(403,detail="you are not allowed to update this blog")
    
    body = body.model_dump()
    for field,value in body.items():
        setattr(one_blog,field,value)

        db.add(one_blog)
        db.commit()
        db.refresh(one_blog)
        return one_blog

def delete_blog(blog_id:int,db:Session,user:UserModel):
    one_blog = db.query(BlogModel).get(blog_id)
    if not one_blog:
        raise HTTPException(404,detail="blog id is incorrect")
    if one_blog.user_id != user.id:
        raise HTTPException(403,detail="you are not allowed to delete this blog")
    
    db.delete(one_blog)
    db.commit()
    return None