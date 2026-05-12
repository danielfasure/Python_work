from fastapi import FastAPI
from models.cake_user import *
from models.cake_user_pydantics import *


app = FastAPI()

cakes_user = sample_user.sample_cake_users

@app.put("/cakes/")
async def updatebook (updateusers: cakeUserValidate):
    for i in range(len(cakes_user)):
        if cakes_user[i].id == updateusers.id:
            cake_user[i] = updateusers
