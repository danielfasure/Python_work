class basic_user:
    name = str
    age = int

    def __init__(self, name, age):
        self.name=name
        self.age=age

    def who_am_i(self):
        print(f' you aew {self.name} and you are currently {self.age} years old, this is a basic user')

class paying_user(basic_user):
    balance = int


    def __init__(self,name,age,balance):
        super().__init__(name=name,age=age)
        self.__balance=balance

    def who_am_i(self):
        print(f' you are {self.name} and you are currently {self.age} years old, this is a paying user with {self.__balance} left on there account')




