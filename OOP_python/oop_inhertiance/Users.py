class general_user:
    email=str

    def __init__(self, email):
        self.__email = email
    def initinaste(self):
        print(f'you have only create a general user with email {self.__email} ')





class subsriced_user(general_user):#the class that you want to inherintant should be passed as an argument
  firstname= str
  lastname= str


  def __init__(self,firstname,lastname,email):
    super().__init__ (email=email)
    self.firstname = firstname
    self.lastname = lastname

  def initinaste(self):
    print(f'you have only create a subsriced user named {self.firstname} {self.lastname} ')



