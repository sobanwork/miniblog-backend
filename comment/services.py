from . import models, schemas
from core.db import get_db      
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

def create_comment(id:int, data:schemas.CommentCreate, db:Session=Depends(get_db)):
    instance = models.Comment(post_id=id, content=data.content, user_id=data.user_id)
    db.add(instance)
    db.commit()
    db.refresh(instance)
    return instance 

def getall_comments(id:int, db:Session=Depends(get_db)):
    comments = db.query(models.Comment).filter(models.Comment.post_id==id).all()
    if comments is None:
        raise HTTPException(status_code=404, detail="No comments found")
    return comments