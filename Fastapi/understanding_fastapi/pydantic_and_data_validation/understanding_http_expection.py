#when you get an result that isnt expected that
#you can import http exception, and it allows for a status code to be displayed when user input an incorrect input or search that pass the validation
#for put and delete request that are succescfull using starlette you can use status class to give user a response to say user updated or deleted

from fastapi import FastAPI,Path,Query,HTTPException


from models.cake_user import *
from models.cake_user_pydantics import *
from starlette import status

cakes = sample_user.sample_cake_users
app = FastAPI()
@app.get("/cake/",status_code=status.HTTP_200_OK)# adding the parameter status code when the fast api read this annotation it knows that a succesfull get should display 200
async def get_user_by_title(userinput:str = Query(min_length = 0)):#query search that return exception if user pass validation
    user_found = False
    cakes_user = []
    for user in cakes:
        if user.title==userinput:
            user_found = True
            cakes_user.append(user)
    if not user_found:
        raise HTTPException(status_code=404,detail='user is not present in list please type another id ')#400 mean client error in this case searching for something out of the range

    else:
        return cakes_user


def createcke_id(cakeuser:cake_user):
    if not len(cakes)== 0:
        cakeuser.id == cakes[-1].id + 1
    else:
        cakeuser.id = 1




@app.post("/cake/",status_code=status.HTTP_201_CREATED)
async def create_user_input(cakesuser: cakeUserValidate):
    created_user = cake_user(cakesuser.dict())
    cakes.append(createcke_id(created_user))



@app.put("/cake_cake_update",status_code=status.HTTP_202_ACCEPTED)
async def update_user_input (cake_user: cakeUserValidate):
    found_user = False
    for x in range(len(cakes)):
        if cakes[x].id == cake_user.id:
           cakes[x]=cake_user
           found_user = True
    if not found_user:
        raise HTTPException(status_code=404,detail='user is not present in list and cannot be updated ')


@app.delete("/cake_cake_delete",status_code=status.HTTP_202_ACCEPTED)
async def delete_user_input (cake_user: cakeUserValidate):
    found_user = False
    for x in range(len(cakes)):
        if cakes[x].id == cake_user.id:
            cakes[x].pop()
            found_user = True
            return "user deleted successfully"
    if not found_user:
        raise HTTPException(status_code=404,detail='user is not present in list and cannot be deleted ')



@app.get("/cake/{user_id}",status_code=status.HTTP_200_OK)
async def get_userbyid(user_id:int = Path(gt =-1)):
    for user in cakes:
        if user.id==user_id:
            return user
    raise HTTPException(status_code=404,detail='user is not present in list ')





