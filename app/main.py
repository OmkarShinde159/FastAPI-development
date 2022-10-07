

from fastapi import FastAPI
from .database import engine
from .import models
from .Routers import post,user,auth,vote
from .config import settings

# print(settings.database_username)

# models.Base.metadata.create_all(bind=engine)

# FastAPI instance : app
app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "Hello World"}

