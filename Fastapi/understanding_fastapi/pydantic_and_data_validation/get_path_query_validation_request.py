#you want to be able to check if the book exist
# you want to check that the search values are within the range to be suspected and not produced searching error
#fast api come with an class clled path that allow for the validation to be done on path request same for queires


from fastapi import FastAPI,Path,Query
from models.cake_user import *


cakes = sample_user.sample_cake_users
app = FastAPI()

@app.get("/user/{user_id}")
async def understanding_pathqueires(user_id: int =Path(gt = 0 ,lt =1000)):
    for user in cakes:
        if user.id == user_id:
            return user


@app.get("/user/getfirstname/")
async def understanding_queires(user_name: str =Query(min_length = 0 ,max_length =1000)):
    user_with_that_name = []
    for user in cakes:
        if user.id == user_name:
           user_with_that_name.append(user.first_name)
