from fastapi import APIRouter,Depends
from . import services,schemas
from .connection import get_db
from .schemas import UserCreate
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/create")
def create_user(data:schemas.UserCreate,db:Session=Depends(get_db))
    return services.create_user(data=data, db=db ) 