class general_user:
    email:str

    def __init__(self,email):
        self.__email = email

    def user_added(self):
        print(f'"congrats you have added {self.__email}"')