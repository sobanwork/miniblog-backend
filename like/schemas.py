from pydantic import BaseModel

class CommentLike(BaseModel):
    post_id: int
    user_id: int

class CommentLikeOut(CommentLike):
    id: int

    class Config:
        from_attributes = True
