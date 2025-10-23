from pydantic import BaseModel

class CommentCreate(BaseModel):
    post_id: int
    user_id: int
    content: str

class CommentOut(CommentCreate):
    id:int

    class Config:
        from_attributes = True