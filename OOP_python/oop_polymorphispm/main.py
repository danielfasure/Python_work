from users import *
def who_is_being_called(current_user:basic_user ):# method called changed based on which child is being called
    current_user.who_am_i()


user1=basic_user("daniel",25)
user2= paying_user("daniel",25,500)
who_is_being_called(user1)
who_is_being_called(user2)
