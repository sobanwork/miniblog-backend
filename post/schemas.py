from pydantic import BaseModel

class PostCreate(BaseModel):
    title: str
    content: str
    tags:str | None = None
    
class PostUpdate(PostCreate):
    pass    

class PostDelete(BaseModel):
    id: int

class PostOut(PostCreate):
    id: int
    

    class Config:
        from_attributes = True
