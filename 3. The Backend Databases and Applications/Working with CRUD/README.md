# Key Learning points for Working with CRUD



## Table of contents

1. Working with CRUD




## 1. Working with CRUD

__CRUD__ - Create, Read, Update, Delete

__Object-Rational Mapping (ORM)__ - object-relational mappers. ORMs help transform Python object to SQL statement and gets result from the  database.

### Creating a Database

Restaurant: name, id
MenuItem: name, id, description, price, course, restaurant_id

restaurant_id is a foreign key that will assign relation to table restaurant (id column)/


[__SQLAlchemy__](http://www.sqlalchemy.org/)
With SQLAlchemy we can write a single python file to set up a database.

Creating database using ```SQLAlchemy``` has few major components:
- __Configuration__:
  - used for importing necessary modules,
  - creates instances of declarative base,
  - creates (or connects) the database and adds tables to columns.
- __Class__: used to represent data in python,
- __Table__: represents specific table in the database,
- __Mapper__: links the columns of the table to the classes that represent them.

### Create a Database - Class and Table

Class code is an object oriented representation  of table in the database. It Extends from the Base class.

Inside the class declaration we will add table and mapper code. Mapper code will create variables that will use to create columns in our database. Those columns have to include number of attributes.

Full code is included in database_setup.py file.

### CRUD create
```python
# Import independencies
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem
# Create engine function
engine = create_engine('sqlite:///restaurantmenu.db')
# Bind engine to the Base Class
Base.metadata.bind = engine
# Create communication between code and selected engine
DBSession = sessionmaker(bind = engine)
# Create instance of DBSession
session = DBSession()
# Create new restaurant
myFirstRestaurant = Restaurant(name = "Pizza Palace")
# Add new restaurant to the staging zone to be committed
session.add(myFirstRestaurant)
# Commit to the database
session.commit()
session.query(Restaurant).all()
# Add MenuItem
cheesepizza = MenuItem(name = "Cheese Pizza", description = "Made with all natural ingridients", course = "Entree", price = "$8.99", restaurant = myFirstRestaurant)
session.add(cheesepizza)
session.commit()
session.query(MenuItem).all()
```

Read from the database

```python
firstResult = session.query(Restaurant).first()
firstResult.name
```

run lotsofrestaurants.py

```Python
# View all restaurants
session.query(Restaurants).all()
```

If we want to view data in more structured way:

```Python
items = session.query(MenuItem).all()
for item in items:
  print item.name
```
