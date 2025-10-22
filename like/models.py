from core.db import Base
from sqlalchemy import Column, Integer, String

class Like(Base):
        __tablename__= "likes"

        id = Column(Integer, primary_key=True, index =True)
        post_id= Column(Integer, index=True)
        user_id= Column(Integer, index=True)