from connection import get_db
from schemas import UserCreate, TokenData
from sqlalchemy.orm import Session
from . import models
from datetime import datetime, timedelta
from typing import Annotated
from jose import JWTError, jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from schemas import Register


SECRET_KEY = "151aba" 
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_user(data:Register, db:Session=Depends(get_db)):
    instance = models.User(email=data.email, username=data.username,password=data.password)
    db.add(instance)
    db.commit()
    db.refresh(instance)
    return 

def login_user(data:UserCreate, db:Session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.email==data.email, models.User.password==data.password).first()
    if not user:
        raise HTTPException(status_code=400, detail="Invalid Credentials")
    access_token = create_access_token(data={"sub": str(user.id)})
    return {"access_token": access_token, "token_type": "bearer"}

def get_current_user(token: str = Depends(OAuth2PasswordBearer(tokenUrl="auth/login")), db: Session = Depends(get_db)):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            user_id: str = payload.get("sub")
            if user_id is None:
                raise credentials_exception
            #token_data = TokenData(username=user_id )
        except JWTError:
            raise credentials_exception
        user = db.query(models.User).filter(models.User.id == int(user_id)).first()
        if user is None:
            raise credentials_exception
        return user


def create_access_token(data: dict):
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

