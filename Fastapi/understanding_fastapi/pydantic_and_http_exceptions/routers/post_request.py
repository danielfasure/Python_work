from models.cake_user import *
from models.cake_user_pydantics import *
from fastapi import Body, APIRouter



router = APIRouter()
cakes= sample_user.sample_cake_users

@router.get("/user/)")
async def get_user():
    return cakes

@router.post("/cake")
async  def adding_validate_data(cake_user1: cakeUserValidate):#you pass in the pydtanic class to be validate
    validate_user_addtion = cake_user(**cake_user1.model_dump()) # if valdate create another user and add it to the databse
    cakes.append(add_user_id(validate_user_addtion))


def add_user_id (users: cake_user):
    if len(cakes) > 0:
        users.id = cakes[-1].id+1 #this mean look at the last id and add 1
    else:
        users.id = 1

    return users #this user now has an id


