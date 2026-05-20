
from models.models import *
from models.models_valdations import *
from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException,Path,Query
from starlette import status
from database.database import SessionLocal
from routers.user_handler import get_current_user

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
db_dependency = Annotated[Session,Depends(get_db)]
cake_dependency = Annotated[dict,Depends(get_current_user)]

@router.get("/", status_code=status.HTTP_200_OK)
async def read_all(db: db_dependency): # depend is adding in dependencies injection
    return db.query(Cake).all()
@router.get("/l", status_code=status.HTTP_200_OK)
async def read_all(db: db_dependency): # depend is adding in dependencies injection
    return db.query(User).all()
"""    
 class Cake(Base):
    __tablename__ = "cake"
    id = Column(Integer,primary_key=True,index=True)
    flavor = Column(String)
    number_of_layers = Column(Integer)
    frosting= Column(Boolean,default=False)
    user_assigned = Column(Integer,ForeignKey("user.id"))

"""


@router.post("/cake/createcake",status_code=status.HTTP_201_CREATED)
async def create_cake(cake_user:cake_dependency,db: db_dependency, cake:cake_validation):
    if cake_user is None:
        raise HTTPException(status_code=401, detail="User not found")
    cake_new_model = Cake(**cake.dict(),user_assigned=cake_user.get('id'))
    db.add(cake_new_model)
    db.commit()


@router.get("/cake/gettingcakes")
async def get_user_cake(cake_user:cake_dependency,db:db_dependency):
    return db.query(Cake).filter(Cake.user_assigned==cake_user.get('id')).all()    

@router.put("/cake/updated_cake",status_code=status.HTTP_200_OK)
async def update_cake(db: db_dependency, cake_id:int, cake:cake_validation):
    cake_model = db.query(Cake).filter(Cake.id == cake_id).first()
    if cake_model is None:
        raise HTTPException(status_code=404, detail="User not found")
    cake_model.flavor = cake.flavor
    cake_model.number_of_layers = cake.number_of_layers
    cake_model.frosting = cake.frosting
    cake_model.user_assigned =  cake.user_assigned


    db.add(cake_model)
    db.commit()

@router.delete("/cake/delete_cake/{cake_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(db: db_dependency, cake_id:int = Path(gt =0)):
    user_model = db.query(Cake).filter(Cake.id == cake_id).first()
    if user_model is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.query(User).filter(Cake.id == cake_id).delete()
    db.commit()

@router.get("/user/{cake_id}",status_code=status.HTTP_200_OK)
async def  read_user_by_id(db:db_dependency, cake_id:int = Path(gt =0)):
    user_model = db.query(Cake).filter(User.id == cake_id).first()
    if user_model is not None:
        return user_model
    raise HTTPException(status_code=404, detail="User not found")