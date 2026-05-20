from database.database import Base
from sqlalchemy import Column,Integer,String,Boolean,ForeignKey

class Cake(Base):
    __tablename__ = "cake"
    id = Column(Integer,primary_key=True,index=True)
    flavor = Column(String)
    number_of_layers = Column(Integer)
    frosting= Column(Boolean,default=False)
    user_assigned = Column(Integer,ForeignKey("user.id"))




class User(Base):
    __tablename__ = "user"
    id = Column(Integer,primary_key=True,index=True)
    username = Column(String)
    email = Column(String)
    hash_password = Column(String)
    has_paid = Column(Boolean,default=False)
    role = Column(String)

