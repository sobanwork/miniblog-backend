from . import models, schemas, services
from core.db import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter(tags=["Follow"])

@router.post("/follow/{user_id}", response_model=schemas.FollowOut)
def follow_user(user_id: int, data: schemas.FollowCreate, db: Session = Depends(get_db)):
    return services.follow_user(user_id=user_id, data=data, db=db)