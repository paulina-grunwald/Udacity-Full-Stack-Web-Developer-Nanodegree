# Import modules
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from datetime import datetime

# Create instance of the declarative base
Base = declarative_base()

class Category(Base):
	# Add table representation
	__tablename__ = "category"
	# Add mappers with attributes
	id = Column(Integer, primary_key = True)
	name = Column(String(250), nullable = False)
	dishes = relationship("Dish", cascade="all, delete-orphan")

class Dish(Base):
	# Add table representation
	__tablename__ = "dish"
	# Add mappers with attributes
	name = Column(String(80), nullable = False)
	id = Column(Integer, primary_key = True)
	description = Column(String(250))
	createdDate = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)
	image = Column(String)
	course = Column(String(250))
	category_id = Column(Integer, ForeignKey('category.id'))
	category = relationship(Category)



# Create instance of create_engine class
engine = create_engine('sqlite:///japanesefood.db')

# Goes to database and adds classes
Base.metadata.create_all(engine)
