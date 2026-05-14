#here is wheee we link the connection between fastapi and the databse

from typing import Annotated

from fastapi import FastAPI, Depends, HTTPException,Path,Query

from sqlalchemy.orm import Session

#from user_pydantic_validate import *
from database.databse import SessionLocal, engine, Base
#from user_database_models import User
from routers import user_request

from starlette import status

app=FastAPI()

app.include_router(user_request.router)

Base.metadata.create_all(bind=engine) #




