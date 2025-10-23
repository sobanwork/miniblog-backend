from . import models, schemas
from core.db import get_db
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

def follow_user(user_id:int, data:schemas.FollowCreate, db:Session=Depends(get_db)):
    instance = models.Follow(follower_id=data.follower_id, following_id=user_id)
    db.add(instance)
    db.commit()
    db.refresh(instance)
    return instance