# Key Learning points for Working with CRUD


## Table of contents

1. [Working with CRUD](#working-with-crud)
2. [Making a Web Server](#making-a-web-server)
3. [Developing with frameworks](#developing-with-frameworks)
4. [Iterative Development](#iterative-development)
5. [Authentication vs Authorization](#authentication-vs-authorization)
6. [Creating Google Sign in](#creating-google-sign-in)
7. [Local Permission System](#local-permission-system)
8. [Adding Facebook and other providers](#adding-facebook-and-other-providers)
9. [What's and Why's of APIs](#whats-and-whys-of-API)
10. [Accessing Published APIs](#accesing-published-APIs)
11. [Creating your own API Endpoints](#creating-API)
12. [Securing your API](#secruting-API)
13. [Writing Developer-Friendly APIs](writing-APIs)

# Working with CRUD

__CRUD__ - Create, Read, Update, Delete

__Object-Rational Mapping (ORM)__ - object-relational mappers. ORMs help transform Python object to SQL statement and gets result from the  database.

### Creating a Database

MenuItems will belong to specific restaurant menu. We will have price and brief description for the menu items. We will have two tables in the restaurantmenu.db:
- ```Restaurant```: name, id
- ```MenuItem```: name, id, description, price, course, restaurant_id

`restaurant_id` is a foreign key that will assign relation to table restaurant (id column)/


With [__SQLAlchemy__](http://www.sqlalchemy.org/) we can write a single python file to set up a database.

Creating database using ```SQLAlchemy``` has few major components:
- ``Configuration``:
  - used for importing necessary modules,
  - creates instances of declarative base,
  - creates (or connects) the database and adds tables to columns.
- ``Class``: used to represent data in Python,
- ``Table``: represents specific table in the database,
- ``Mapper``: links the columns of the table to the classes that represent them.

It is necessary to create instance of a class called ```declarative base``` in order for our class to inherit all the features from SQLAlchemy.

### Create a Database - Class and Table

``Class code`` is an object oriented representation  of table in the database. It Extends from the Base class. Inside the class declaration we will add table and mapper code. ```Mapper code``` will create variables that will use to create columns in our database. Those columns have to include number of attributes.

### Interacting with CRUD

Full code is included in ```database_setup.py file```.

```Python
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
```
Few important notes on attibutes:
- string(80) - string can be specified with max. number of characters
- relationship tell SQL what relationship the table has with other tables
- if nullable is false it means that a column entry must have a value in orderfor the row to be created.

Now I will import  the necessary libraries, connect to our restaurantMenu.db, and create a session to interface with the database.

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
# u'Pizza Palace'
```
Run lotsofrestaurants.py.

```Python
# View all restaurants
session.query(Restaurants).all()
```

If we want to run a query in python we need to create:
```python
variable_name = session.query(Table_Name).all()
for item in variable_name:
  print item.table_column
```

```Python
items = session.query(MenuItem).all()
for item in items:
  print item.name
```
```
Cheese Pizza
Veggie Burger
French Fries
Chicken Burger
Chocolate Cake
Sirloin Burger
Root Beer
Iced Tea
etc.
```

To update data in the database we need to follow following steps:
1. Find entry that we want to change
2. Change the value
3. Add to session
4. Commit session

```Python
veggieBurgers = session.query(MenuItem).filter_by(name = 'Veggie Burger')
for veggieBurger in veggieBurgers:
    print veggieBurger.id
    print veggieBurger.price
    print veggieBurger.name
    print "\n"
```

Update price of the veggie burger to $2.99:

```python
UrbanVeggieBurger = session.query(MenuItem).filter_by(id=8).one()
UrbanVeggieBurger.price = '$2.99'
session.add(UrbanVeggieBurger)
session.commit()
```


Delete an item from database:




# 2. Making a Web Server

Protocols help with communication between client and server.
``TCP`` - Transmission Control Protocol - enables information information to be broken into small pieces between client and server.
``IP`` - Internet Protocol - allow messages to be properly routed
``HTTP`` - Hypertext Transfer Protocol
Ports are use to designate channels of the communication on the same ip address.

Ports numbers can range from 0 to 65536.
Local host has ip: 127.0.0.1

#### HTTP and Response Codes
200: Successful GET
301: Successful POST
404: File not found


#### GET and POST
GET:
- good for viewing information that is already on the server
- happen simply by visiting URL in the browser
POST:
- allow user to customize the web experience,
- require data to be submitted e.g post
#### Adding POST to web server

# REFERENCES
- https://www.vagrantup.com/docs/networking/forwarded_ports.html
