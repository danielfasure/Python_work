class daniel_private_user:


    def __init__(self,firstname,lastname,email): #making variable private
        self.__firstname=firstname
        self.__lastname= lastname
        self.__email=email

    def getfirstname(self): #now only when you call the method can you use the value assign to prevent accidental deletion
        return self.__firstname


    def getlastname(self):
        return self.__lastname

    def getemail(self):
        return self.__email


    def setfirstname(self,firstname):#when you call you can now change the value
        self.__firstname=firstname

    def setlastname(self,lastname):
        self.__lastname=lastname

    def setemail(self,email):
        self.__email=email




