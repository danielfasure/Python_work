#this allow for data validation when you want to create an object you need it follow the structure defined below
#using the pydantic py file and importing base model it will create the class and when that class it used it will follow the rules set
from typing import Optional

from pydantic import BaseModel,Field

class cakeUserValidate(BaseModel): #this tell fastapi to treat this as a child of pydantic base model
    id: Optional[int]= None #using optional from the class typing allow this field to be none
    title: str = Field(min_length=1,max_length=100)# mean min lenght it 1 character and max lenght is 1000
    firstname: str = Field(min_length=1,max_length=100)
    lastname: str = Field(min_length=1,max_length=100)
    email: str = Field(min_length=1,max_length=100)
    #age : int =Field (gt =-1, lt= 300)  # value that can input need to be between zero and 299
