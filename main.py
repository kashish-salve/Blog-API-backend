from fastapi import FastAPI
from src.utils.db import Base,engine
from src.user.routes import user_routes
from src.blog.routes import blog_routes
from src.comment.routes import comment_routes
from src.like.routes import like_routes

Base.metadata.create_all(engine)


app = FastAPI()
app.include_router(user_routes)
app.include_router(blog_routes)
app.include_router(comment_routes)
app.include_router(like_routes)