from sqlalchemy import Integer,Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
import uuid
from core.db import Base

class Post(Base):
        __tablename__= "posts"
        id = Column(Integer, primary_key=True, index =True)
        title = Column(String, index=True)
        content = Column(String, index=True)
        tags=Column(String, index=True, nullable=True)
        created_at= Column(DateTime, default=datetime.utcnow)
        updated_at= Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
        author_id= Column(Integer, index=True)
        


