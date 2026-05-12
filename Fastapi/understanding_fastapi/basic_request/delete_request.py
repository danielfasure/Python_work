
from fastapi import Body, FastAPI

from models.cakes import cakes

app = FastAPI()
cakes = cakes.list_of_cakes


@app.get("/cakes/see_cakes")
async def see_cakes():
    return cakes

@app.delete("/cakes/delete/{cake_title}")
async def delete_cake(cake_title = str ):
    for i in range(len(cakes)):
        if cakes[i].get('caketitle').casefold()== cake_title.casefold():
            cakes.pop(i)
            break
