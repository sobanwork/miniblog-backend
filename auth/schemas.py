from pydantic import BaseModel


class Register(BaseModel):
    email:str
    username:str
    password:str

class Login(BaseModel):
    username:str
    password:str

class Logout(BaseModel):
    email:str

class UserUpdate(Register):
    id:int

class UserDelete(BaseModel):
    id:int

class UserOut(BaseModel):
    id:int


    class Config:
        orm_mode = True



class Token(BaseModel):
    access_token: str
    token_type: str
class TokenData(BaseModel):
    username: str | None = None 
