"""
functions are resuable pieces of code used to perform a task when called apon 

def is the keywords used to define them and to call the function (name_of_function())


"""

def first_function():
    print("inside the function yooo")

first_function()

"""
assignment 
"""

def create_user(firstname,lastname,age):
    user= {"first_name":firstname, "last name": lastname, "age":age}
    return user

daniel_user = create_user(firstname="daniel", lastname="fasure",age=25)    
print(daniel_user)