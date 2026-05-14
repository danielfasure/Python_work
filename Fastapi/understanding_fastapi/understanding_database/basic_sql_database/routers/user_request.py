
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException,Path,Query

from sqlalchemy.orm import Session

from model_and_validation.user_pydantic_validate import *
from database.databse import SessionLocal, engine, Base
from model_and_validation.user_database_models import User

from starlette import status


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
db_dependency = Annotated[Session,Depends(get_db)]

@router.get("/", status_code=status.HTTP_200_OK)
async def read_all(db: db_dependency): # depend is adding in dependencies injection
    return db.query(User).all()


@router.post("/user/createuser",status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency, user:User_validate):
    user_new_model = User(**user.dict())
    db.add(user_new_model)
    db.commit()

@router.put("/user/updated_user",status_code=status.HTTP_200_OK)
async def update_user(db: db_dependency, user_id:int, user:User_validate):
    user_model = db.query(User).filter(User.id == user_id).first()
    if user_model is None:
        raise HTTPException(status_code=404, detail="User not found")
    user_model.username = user.username
    user_model.paid = user.paid
    user_model.email = user.email
    db.add(user_model)
    db.commit()

@router.delete("/user/delete_user/{user_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(db: db_dependency, user_id:int = Path(gt =0)):
    user_model = db.query(User).filter(User.id == user_id).first()
    if user_model is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.query(User).filter(User.id == user_id).delete()
    db.commit()

@router.get("/user/{user_id}",status_code=status.HTTP_200_OK)
async def  read_user_by_id(db:db_dependency, user_id:int = Path(gt =0)):
    user_model = db.query(User).filter(User.id == user_id).first()
    if user_model is not None:
        return user_model
    raise HTTPException(status_code=404, detail="User not found")