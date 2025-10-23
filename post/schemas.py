from pydantic import BaseModel
from datetime import datetime

class PostCreate(BaseModel):
    title: str
    content: str
    tags:str | None = None
    created_at: datetime
    updated_at: datetime
    author_id: int 

    
class PostUpdate(PostCreate):
    pass    

class PostDelete(BaseModel):
    id: int

class PostOut(PostCreate):
    id: int
    

    class Config:
        from_attributes = True
