from fastapi import APIRouter


router = APIRouter()
from models.cake_user import *
from models.cake_user_pydantics import *


@router.get("/delete_user")
async def delete_user(user_id: int):
    for i in range(len(sample_user.sample_cake_users)):
        if sample_user.sample_cake_users[i].id == user_id:
            sample_user.sample_cake_users.pop(i)