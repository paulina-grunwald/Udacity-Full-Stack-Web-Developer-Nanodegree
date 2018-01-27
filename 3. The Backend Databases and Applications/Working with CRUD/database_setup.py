# Import modules
import sys
import sqlalchemy import 
Column, ForeginKey, Integer, String

from sqlalchemy.ext.declarative import declarative database

from sqlalchemy.orm import relationship 

from sqlalchemy import create_engine 

# Create instance of the declarative base
Base = declarative_base()

class Restaurant(Base):
	__tablename__ = "restaurant"
	name = Column(String(80), nullable = False)
	id = Column(Integer, primary_key = True)



class MenuItem(Base):
	__tablename__ = "menu_item"
	name = 
	id =
	course =
	description =
	restaurant_id = 
	restaurant = relationship(Restaurant)



# Create instance of create_engine class
engine = create_engine('sqlite://restaurantmenu.db')

# Goes to database and adds classes
Base.metadata.create_all(engine)