from fastapi import APIRouter,Depends
from . import services,schemas
from MINIBLOG-BACKEND.connection import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/posts", response_model=schemas.PostCreate)
def create_post(data:schemas.PostCreate,db:Session=Depends(get_db)):
    return services.create_post(data=data, db=db )

@router.get("/posts", response_model=list[schemas.PostOut])
def get_posts(db:Session=Depends(get_db)):
    return services.get_posts(db=db)

@router.get("posts/{post_id}", response_model=schemas.PostCreate)
def get_post_by_id(post_id:int, db:Session=Depends(get_db)):   
    return services.get_post_by_id(post_id=post_id, db=db)

@router.put("posts/{post_id}", response_model=schemas.PostCreate)
def update_post(post_id:int, data:schemas.PostUpdate, db:Session=Depends(get_db)):
    return services.update_post(post_id=post_id, data=data, db=db)

@router.delete("posts/{post_id}", response_model=dict)
def delete_post(post_id:int, db:Session=Depends(get_db)):
    return services.delete_post(post_id=post_id, db=db)

