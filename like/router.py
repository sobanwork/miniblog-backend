from fastapi import APIRouter, Depends
from . import services, schemas
from core.db import get_db
from sqlalchemy.orm import Session


router =APIRouter(tags=["Likes"])

@router.post("/posts/{id}/like", response_model=schemas.CommentLike)
def create_like(id:int, data:schemas.CommentLike, db:Session=Depends(get_db)):
    return services.create_like(id=id, data=data, db=db)