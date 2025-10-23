
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.db import Base, engine
from auth.router import router as auth_router
from post.router import router as post_router
from post import models
from comment.router import router as comment_router
from like.router import router as like_router
from follow.router import router as follow_router
from auth import models as auth_models
from post import models as post_models
from comment import models as comment_models
from like import models as like_models
from follow import models as follow_models


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(post_router)
app.include_router(auth_router)
app.include_router(comment_router)
app.include_router(like_router)
app.include_router(follow_router)
@app.get("/health")
def health():
    return {"status": "ok"}
