class cake_user:
    id: int
    title: str
    firstname: str
    lastname: str
    email: str

    def __init__(self,id,title,firstname,lastname,email):
        self.id = id
        self.title = title
        self.firstname = firstname
        self.lastname = lastname
        self.email = email


class sample_user:
    sample_cake_users= [cake_user(1, 'mr', 'daniel', 'fasure', 'danielfasure@gmail.com'),
                        cake_user(2, 'miss', 'pamela', 'fasure', 'pamelafasure@gmail.co'),
                        cake_user(3, 'dr', 'johhny', 'fedrick', 'jf@gmail.com'),
                        cake_user(4, 'mrs', 'lin', 'parker', 'linparker@gmail.com'),
                        ]
