from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    created_at: str
    bio= str | None = None
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
    bio= str | None = None
    avatar: str | None = None
    social_links: str | None = None
    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
