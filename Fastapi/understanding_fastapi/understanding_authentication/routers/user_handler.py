

from fastapi import APIRouter,HTTPException
from models.models import *
from models.models_valdations import *
from passlib.context import CryptContext



router = APIRouter()

brcrypt_context =CryptContext(schemes=['bcrypt'],deprecated='auto') #setting the alogrithim used to hash password 
@router.post("/login")
async def create_user(user: user_validate):
    created_user = User(username=user.username,
                        email=user.email,
                        has_paid=user.has_paid,
                        role=user.role,

                        hash_password=brcrypt_context.hash(user.password))# using it to pass hash password 
    return created_user





