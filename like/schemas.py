from pydantic import BaseModel

class CommentLike(BaseModel):
    post_id: int
    user_id: int

