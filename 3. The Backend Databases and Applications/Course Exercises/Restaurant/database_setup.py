# Import modules
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

# Create instance of the declarative base
Base = declarative_base()

class Restaurant(Base):
	# Add table representation
	__tablename__ = "restaurant"
	# Add mappers with attributes
	id = Column(Integer, primary_key = True)
	name = Column(String(250), nullable = False)

class MenuItem(Base):
	# Add table representation
	__tablename__ = "menu_item"
	# Add mappers with attributes
	name = Column(String(80), nullable = False)
	id = Column(Integer, primary_key = True)
	description = Column(String(250))
	price = Column(String(8))
	course = Column(String(250))
	restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
	restaurant = relationship(Restaurant)



# Create instance of create_engine class
engine = create_engine('sqlite:///restaurantmenu.db')

# Goes to database and adds classes
Base.metadata.create_all(engine)
