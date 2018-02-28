from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Dish

engine = create_engine('sqlite:///japanesefood.db')
Base.metadata.bind=engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

# Below written queries have to be run by copping them into the git bash 
# Query first Category name 
first = session.query(Category).first()
first.name
# u'Rice Dishes'

# Query all the Dishes in the database 
item = session.query(Dish).all()
for item in items:
	print item.name
	print item.description

