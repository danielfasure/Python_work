from fastapi import FastAPI

from typing import Annotated
from routers import cake_handler,user_handler
from models import models
from database import database


from fastapi import FastAPI, Depends, HTTPException,Path,Query

from sqlalchemy.orm import Session
from starlette import status
app = FastAPI()
models.Base.metadata.create_all(bind=database.engine)


app.include_router(cake_handler.router)
app.include_router(user_handler.router)