from oop_parent_user import *
class subscribed_user(general_user):
    first_name = str
    last_name = str
    age = int

    def __init__(self,first_name,last_name,age,email):
        super().__init__(email=email)
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


    def user_added(self):
        print(f'"{self.first_name} {self.last_name} {self.age} has been subscribed to webpage"')
