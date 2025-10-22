from fastapi import APIRouter,Depends
from . import services,schemas
from core.db import get_db
from sqlalchemy.orm import Session


router = APIRouter(tags=["Comment"])

@router.post("/posts/{id}/comment", response_model=schemas.CommentCreate)
def create_comment(id:int, data:schemas.CommentCreate, db:Session=Depends(get_db)):
    return services.create_comment(id=id, data=data, db=db)

@router.get("/posts/{id}/comments", response_model=list[schemas.CommentOut])
def getall_comments(id:int, db:Session=Depends(get_db)):
    return services.getall_comments(id=id, db=db)
