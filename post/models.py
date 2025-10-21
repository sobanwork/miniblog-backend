from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.connection import engine, Base

Base=declarative_base()

class Post(Base):
        __tablename__= "posts"

        id = Column(Integer, primary_key=True, index =True)
        title = Column(String, index=True)
        content = Column(String, index=True)
        tags=Column(String, index=True, nullable=True)
        created_at= Column(DateTime, default=datetime.utcnow)
        updated_at= Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
        author_id= Column(Integer, index=True)
        #user_id= Column(Integer, ForeignKey("users.id"))
        #user= relationship("Users", back_populates="blog")



