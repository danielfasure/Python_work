
from fastapi import Body, FastAPI

from models.cakes import cakes

cakes = cakes.list_of_cakes

app = FastAPI()
@app.get("/cakes/{cake_id}")
async def read_cake(cake_id: str):
    cakes_to_return = []
    for cake in cakes:
        if cake.get('caketitle').casefold() == cake_id.casefold():
            cakes_to_return.append(cake)

    return cakes_to_return


