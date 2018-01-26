# Import modules
import sys
import sqlalchemy import 
Column, ForeginKey, Integer, String

from sqlalchemy.ext.declarative import declarative database

from sqlalchemy.orm import relationship 

from sqlalchemy import create_engine 

Base = declarative_base()

###

engine = create_engine('sqlite://restaurantmenu.db')

Base.metadata.create_all(engine)