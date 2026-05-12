#allow for the user to see data stored behind the endpoint code


# allow the data the user has inputted to be stored inside a server
# to input data into server
# in the CRUD it is the same as a Create request
from fastapi import FastAPI
from pydantic import BaseModel
from models.cakes import cakes

app = FastAPI()
books = cakes.list_of_cakes
@app.get("/")#at the url return the code below
async def first_api():
    return {"message": "Hello World"}, books


#query parameter
#request parameters that have been attached after ?
#have a name=value pairs
# a post reuest with url 127.0.0.1:8000/books/?flavour=chocolate

@app.get("/cakes/")
async def get_cakes_flavour(flavour: str):
    list_of_cakes = []
    for cake in books:
        if cake.get('flavour').casefold() == flavour.casefold():
            list_of_cakes.append(cake)
    return list_of_cakes

#dynamic parameter/ path parameter
#allow the url to be read and used as a value to showcase data
#when using dynamic parameter it will be looked at first before static api call

@app.get("/cakes/{cake_title}")#
async def get_cake(cake_title: str):
    for cake in books:
        if cake.get('caketitle').casefold() == cake_title.casefold():
            return cake
