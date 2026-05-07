from OOP_python.oop_abstraction.oop_user_class import *
from class_parameter_constructor import *
from OOP_python.oop_encapsulation.oop_user_encapsulation import *
from oop_child_user import *

daniel_general= general_user("danielfasure.gmail.com")
daniel_general.user_added()
daniel_subsrcibed= subscribed_user("daniel","fasure",25,"danielfasure@gmail.com")
daniel_subsrcibed.user_added()


daniel_private_user = daniel_private_user("daniel","fasure","daniel.fasure@gmail.com2")


main_user = daniel_user()
print(main_user.name)

daniel = daniel_user_parmeters("daniel","fasure",25,"danielfasure@Gmail.com")
print(daniel.firstname)
daniel.talk()