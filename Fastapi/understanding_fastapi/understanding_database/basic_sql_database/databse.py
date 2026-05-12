#in this py file url string is ccreated to estisblish an connection between the code and databse
#pip install sqlalchemy to allow python to estiblisation connection
# for databse connection you need a url, engine,session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


SQLALCHEMY_DATABASE_URL = 'sqlite:///./cakes.db' # where the database is store

engine = create_engine(SQLALCHEMY_DATABASE_URL,connect_args={"check_same_thread":False})# argument we want to pass into the engine in this case only allow one thread to connect at a time

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)# by removing all the auto commit and flush control of what get saved is soley on the user code


Base = declarative_base()