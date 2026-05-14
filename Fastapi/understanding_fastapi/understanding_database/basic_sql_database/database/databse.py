#sqlalchemy read this py file and know this where the engine, session, base are stored used to communacte with the database
#
#using the url will connect the fast api application to the databse sqlite
# for databse connection you need a url, engine,session,base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


SQLALCHEMY_DATABASE_URL = 'sqlite:///./cakes.db' # where the database is store, and created
#
engine = create_engine(SQLALCHEMY_DATABASE_URL,connect_args={"check_same_thread":False})#connect to the database and enforces that the data can be write once at a time
#sesion maker allow you to save and make api request allow the crud operation
#act like a factory where you can host the operation and tools
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)# this is the manager for the database where it allow for the data to be read and writing based on the configuration of the engine and other factor


Base = declarative_base() # blueprint of the database table for model allow the class to use colummns and primary key and more table features