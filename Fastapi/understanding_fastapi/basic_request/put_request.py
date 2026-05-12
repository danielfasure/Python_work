#allow update of dat stored by identify the data you want you want to alter and changing it



from fastapi import Body, FastAPI

from models.cakes import cakes

cakes = cakes.list_of_cakes

app = FastAPI()

@app.get("/cakes")
async def showcase_cakes():
    return cakes


#put is used to update you pass the object you want to update and can modify what you want
@app.put("/cakes")
async def update_cake(updated_cake=Body()):
    for i in range(len(cakes)):
        if cakes[i].get('caketitle') == updated_cake.get('caketitle'):
            cakes[i] = updated_cake



