from fastapi import APIRouter
from models.cake_user import *


cakes = sample_user.sample_cake_users
router = APIRouter()

@router.get("/hello")
async def read_query(firstname: str):
    cakes_that_match = []
    for cake in cakes:
        if cake.firstname == firstname:
            cakes_that_match.append(cake)

    return cakes_that_match

@router.get("/cake/{id}")
async def read_id(id : int):
    for cake in cakes:
        if cake.id == id:
           return cake
