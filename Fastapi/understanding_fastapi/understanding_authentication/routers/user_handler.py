from urllib.request import Request

from fastapi import APIRouter
from models.models import *
from models.models_valdations import *


router = APIRouter()
@router.post("/login")
async def create_user(user: user_validate):
    created_user = User(username=user.username,
                        email=user.email,
                        has_paid=user.has_paid,
                        role=user.role,
                        hash_password=user.password)
    return created_user





