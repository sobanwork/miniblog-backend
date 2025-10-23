from pydantic import BaseModel  

class FollowCreate(BaseModel):
    follower_id: int
    following_id: int

class FollowOut(FollowCreate):
    id: int

    class Config:
        from_attributes = True