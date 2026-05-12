from pydantic import BaseModel,Field
class User_validate(BaseModel):
    username : str =Field(min_length=5,max_length=50)
    email : str =Field(min_length=2,max_length=200)
    paid : bool
