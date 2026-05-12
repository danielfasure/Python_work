#creating the table but here will be how we model the database
from operator import index

#need to add the base from the database py file
from databse import Base
from sqlalchemy import Column,Integer,String,Boolean

class User(Base): # this class is now a child of the database declecteractive base model and will allow for the creation of database table
    __tablename__ = 'user' # define the name of the table

    id = Column(Integer,primary_key=True,index=True) #we import column class and integer class to tell the database to define as header for the colums also can add parameter to say that this colums is the primary key so all values should be unique
    username = Column(String(50))
    email = Column(String(50),nullable=False)
    paid = Column(Boolean,default=False)




