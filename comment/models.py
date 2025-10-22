from core.db import Base
from sqlalchemy import Column, Integer, String

class Comment(Base):
        __tablename__= "comments"

        id = Column(Integer, primary_key=True, index =True)
        content = Column(String, index=True)
        post_id= Column(Integer, index=True)
        user_id= Column(Integer, index=True)