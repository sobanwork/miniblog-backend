from . import models, schemas
from core.db import get_db
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

def create_like(id:int, data:schemas.CommentLike, db:Session=Depends(get_db)):
    instance = models.Like(post_id=id, user_id=data.user_id)
    db.add(instance)
    db.commit()
    db.refresh(instance)
    return instance