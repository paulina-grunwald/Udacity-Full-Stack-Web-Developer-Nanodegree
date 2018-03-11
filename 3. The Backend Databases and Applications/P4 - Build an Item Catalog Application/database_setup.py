# Import modules
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
import datetime

# Create instance of the declarative base
Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))

    @property
    def serialize(self):
    	return {
    		'name' : self.name,
    		'id' : self.id,
    	}

class Category(Base):
	# Add table representation
	__tablename__ = "category"
	# Add mappers with attributes
	id = Column(Integer, primary_key = True)
	name = Column(String(250), nullable = False)
	dishes = relationship("Dish", cascade="all, delete-orphan")
	user_id = Column(Integer, ForeignKey('user.id'))

	@property
	def serialize(self):
		return {
			'name'	:	self.name,
			'id'	:	self.id,
			'user_id' : self.user_id
		}


class Dish(Base):
	# Add table representation
	__tablename__ = "dish"
	# Add mappers with attributes
	name = Column(String(80), nullable = False)
	id = Column(Integer, primary_key = True)
	description = Column(String(250))
	createdDate = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)
	image = Column(String)
	category_id = Column(Integer, ForeignKey('category.id'))
	category = relationship(Category)
	user_id = Column(Integer, ForeignKey('user.id'))
	user = relationship(User)

	@property
	def serialize(self):
		return {
			'name' : self.name,
			'id' : self.id,
			'description' : self.description,
			'user_id': self.user_id
		} 

   

# Create instance of create_engine class
engine = create_engine('sqlite:///japanesefood.db')

# Goes to database and adds classes
Base.metadata.create_all(engine)
