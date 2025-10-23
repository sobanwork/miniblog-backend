import psycopg2
from psycopg2 import OperationalError

def test_connection():
    try:
        connection = psycopg2.connect(
            dbname="db",          # your database name
            user="postgres",      # your PostgreSQL username
            password="123456",    # your PostgreSQL password
            host="localhost",     # host, e.g., localhost or IP
            port="5432"           # port number
        )
        print("Connection successful")
        connection.close()
    except OperationalError as e:
        print(f"Connection failed: {e}")

test_connection()


def get_profile_by_username(username: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

def update_profile(data: UserUpdate, db: Session = Depends(get_db)):

    user = db.query(User).filter(User.username == data.username).first()
    update_user = data.dict(exclude_unset=True)
    for key,value in update_user.items():
        setattr(user, key, value)
    db.commit()
    db.refresh(user)
    return user


 from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    created_at: datetime
    bio: str | None = None
    avatar: str | None = None
    social_links: str | None = None


class UserUpdate(UserCreate):
    pass

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class ProfileOut(BaseModel):
    id: int
    email: EmailStr
    password: str
    created_at: str
    bio: str #| None = None
    avatar: str #| None = None
    social_links: str # | None = None
    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


@router.put("/profile/update", response_model=schemas.ProfileOut)
def update_profile(payload: schemas.UserUpdate, db: Session = Depends(get_db), request: Request = None):
    return service.update_profile(data=payload, db=db)

@router.get("/profile/{username}", response_model=schemas.ProfileOut)
def get_profile_by_username(username: str, db: Session = Depends(get_db)):
    return service.get_profile_by_username(username=username, db=db)
    

    class User(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    bio = Column(String, nullable=True)
    avatar= Column(String, nullable=True)
    social_links = Column(String, nullable=True)