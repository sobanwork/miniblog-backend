import os
from dotenv import load_dotenv
load_dotenv()

class Settings:
    DATABASE_URL = os.getenv("DATABASE_URL")
    JWT_SECRET = os.getenv("JWT_SECRET")
    JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60))
settings = Settings()
