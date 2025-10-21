from post.routers import router as post_router
from auth.routers import router as auth_router
from fastapi import FastAPI
app = FastAPI()
app.include_router(post_router, tags=["posts"])
app.include_router(auth_router, prefix="/auth", tags=["auth"])

