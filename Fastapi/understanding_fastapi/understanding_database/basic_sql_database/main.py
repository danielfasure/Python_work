#here is wheee we link the connection between fastapi and the databse

from typing import Annotated

from fastapi import FastAPI, Depends, HTTPException,Path,Query

from sqlalchemy.orm import Session

from user_pydantic_validate import *
from databse import SessionLocal, engine, Base
from user_database_models import User
from routers import auth_request

from starlette import status

app=FastAPI()
app.include_router(auth_request.router)

Base.metadata.create_all(bind=engine) #


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_depency = Annotated[Session,Depends(get_db)]  # will check if there is an connection that can happen


@app.get("/", status_code=status.HTTP_200_OK)
async def read_all(db: db_depency): # depend is adding in dependencies injection
    return db.query(User).all()


@app.post("/user/createuser",status_code=status.HTTP_201_CREATED)
async def create_user(db: db_depency,user:User_validate):
    user_new_model = User(**user.dict())
    db.add(user_new_model)
    db.commit()

@app.put("/user/updated_user",status_code=status.HTTP_200_OK)
async def update_user(db: db_depency,user_id:int,user:User_validate):
    user_model = db.query(User).filter(User.id == user_id).first()
    if user_model is None:
        raise HTTPException(status_code=404, detail="User not found")
    user_model.username = user.username
    user_model.paid = user.paid
    user_model.email = user.email
    db.add(user_model)
    db.commit()

@app.delete("/user/delete_user/{user_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(db: db_depency,user_id:int = Path(gt =0)):
    user_model = db.query(User).filter(User.id == user_id).first()
    if user_model is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.query(User).filter(User.id == user_id).delete()
    db.commit()

@app.get("/user/{user_id}",status_code=status.HTTP_200_OK)
async def  read_user_by_id(db:db_depency,user_id:int = Path(gt =0)):
    user_model = db.query(User).filter(User.id == user_id).first()
    if user_model is not None:
        return user_model
    raise HTTPException(status_code=404, detail="User not found")





