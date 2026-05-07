class starting_user:

    name:str = "daniel"
    age:int = 25
    lastname:str = "fasure"

    def __init__(self,name,age,lastname):
        self.name = name
        self.age = age
        self.lastname = lastname

    def walking(self):
        print(f'{self.name} is walking at the age of {self.age} years')
