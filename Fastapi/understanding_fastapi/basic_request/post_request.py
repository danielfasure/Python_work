# allow the data the user has inputted to be stored inside a server
# to input data into server
# in the CRUD it is the same as a Create request
from fastapi import Body, FastAPI

from models.cakes import cakes
cakes = cakes.list_of_cakes
app = FastAPI()


@app.post("/cakes/create_cake")
async def create_cake(created_cake = Body()):
    cakes.append(created_cake)
    return created_cake



#combining both