from pydantic import BaseModel


class LikeSchema(BaseModel):
    user_id:int
    post_id:int