from . import models, schemas
from core.db import get_db
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session


def create_post(data:schemas.PostCreate, db:Session=Depends(get_db)):
    instance = models.Post(title=data.title, content=data.content, tags=data.tags)
    db.add(instance)
    db.commit()
    db.refresh(instance)
    return instance

def get_posts(db:Session=Depends(get_db)):
    posts = db.query(models.Post).all()
    if posts is None:
        raise HTTPException(status_code=404, detail="No posts found")
    return posts

def get_post_by_id(post_id:int, db:Session=Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id==post_id).first()
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post 

def update_post(post_id:int, data:schemas.PostUpdate, db:Session=Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id==post_id).first()
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    
    post.title = data.title
    post.content = data.content
    post.tags = data.tags
    db.commit()
    db.refresh(post)
    return post

def delete_post(post_id:int, db:Session=Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id==post_id).first()
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    db.delete(post)
    db.commit()
    return {"message":"Post deleted successfully"}