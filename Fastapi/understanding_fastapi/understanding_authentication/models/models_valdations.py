from pydantic import BaseModel

class cake_validation(BaseModel):

    flavor : str
    number_of_layers :int
    frosting :bool


class user_validate(BaseModel):
    username : str
    email : str
    password : str
    has_paid : bool
    role : str
