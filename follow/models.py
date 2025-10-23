from core.db import Base
from sqlalchemy import Column, Integer, String

class Follow(Base):
        __tablename__= "follows"

        id = Column(Integer, primary_key=True, index =True)
        follower_id= Column(Integer, index=True)
        following_id= Column(Integer, index=True)