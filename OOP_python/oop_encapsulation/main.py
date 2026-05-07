from oop_user_encapsulation import *

daniel_user = daniel_private_user(firstname="Daniel",lastname="M",email="daniel.fasure@gmail.com")
print(daniel_user.getemail())
daniel_user.setemail("notdanielfasure@gmail,com")
print(daniel_user.getemail())