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
Few important notes on attributes:
- String(80) - string can be specified with max. number of characters
- Relationship tell SQL what relationship the table has with other tables.
- If nullable is false it means that a column entry must have a value in order for the row to be created.
- Setting primary key to true indicates a value that we can use to uniquely identify each row of our database table.
- ForeginKey is used to make a reference to another table.

### CRUD Create and Update

Now I will import  the necessary libraries, connect to our restaurantMenu.db, and create a session to interface with the database.

```python
# Import independencies
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem
# Create engine function to specify
# To which database we want to connect
engine = create_engine('sqlite:///restaurantmenu.db')
# Bind engine to the Base Class
Base.metadata.bind = engine
# Create communication between code and selected engine
DBSession = sessionmaker(bind = engine)
# Create instance of DBSession
session = DBSession()

# Add new restaurant
myFirstRestaurant = Restaurant(name = "Pizza Palace")
# Add new restaurant to the staging zone to be committed
session.add(myFirstRestaurant)
# Commit to the database
session.commit()

# Find all the entries in Restaurant table and return them in list
session.query(Restaurant).all()

# Add cheesepizza to MenuItem table
cheesepizza = MenuItem(name = "Cheese Pizza", description = "Made with all natural ingredients", course = "Entree", price = "$8.99", restaurant = myFirstRestaurant)

# Add cheesepizza to the session
session.add(cheesepizza)
# Commit the session
session.commit()
# View all entries in MenuItem table
session.query(MenuItem).all()
```

### CRUD Read

Currently we have only one Restaurant in our database. Let's view it:

```python
firstResult = session.query(Restaurant).first()
firstResult.name
# u'Pizza Palace'
```
Now I will run ```lotsofrestaurants.py``` to load more restaurants to my database.

```Python
# View all restaurants
session.query(Restaurants).all()
```

To view all MenuItems in more readable form we need to loop through the result of the query:

```Python
items = session.query(MenuItem).all()
for item in items:
  print item.name

  # Result:
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


### CRUD update

To update data in the database we need to follow following steps:
1. Find entry that we want to change using filter_by function
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

### CRUD Update
Update price of the veggie burger to $2.99:

```python
UrbanVeggieBurger = session.query(MenuItem).filter_by(id=8).one()
UrbanVeggieBurger.price = '$2.99'
session.add(UrbanVeggieBurger)
session.commit()
```

Update price of all Veggie Burgers:

```Python
for veggieBurger in veggieBurgers:
  if veggieBurger.price != '$2.99':
    veggieBurger.price = '$2.99'
    session.add(veggieBurger)
    session.commit()

```
### CRUD Delete

```Python  
spinach = session.query(MenuItem).filter_by(name = 'Spinach Ice Cream').one()
print spinach.restaurant.name
# Auntie Ann's Diner

spinach = session.query(MenuItem).filter_by(name = 'Spinach Ice Cream').all()
for item in spinach:
  print item.id
  print item.name
  print item.price
#  44
#  Spinach Ice Cream
#  $1.99

session.delete(spinach)
session.commit()

```



# Making a Web Server

### Clients, Servers and Protocols

Protocols help with communication between client and server.
``TCP`` - Transmission Control Protocol - enables information information to be broken into small pieces between client and server.
``IP`` - Internet Protocol - allow messages to be properly routed
``HTTP`` - Hypertext Transfer Protocol
Ports are use to designate channels of the communication on the same ip address.
``UDP`` - User Datagram Protocol

Ports numbers can range from 0 to 65536.

Local host has ip: ``127.0.0.1``

#### HTTP and Response Codes
```
200: Successful GET
301: Successful POST
404: File not found
```

#### GET and POST
``GET``:
- good for viewing information that is already on the server
- happen simply by visiting URL in the browser

``POST``:
- allow user to customize the web experience,
- require data to be submitted e.g post


### Adding CRUD to our Website

Objectives for the project:

1. Modify ```webserver.py``` so when we open localhost:8080/restaurants we will see list of the restaurant
2. After name of each restaurant there should be a link to edit or delete restaurant.
3. Add link to the page that will be able to create new restaurants.
4. Users should be able rename selected restaurant.
5. Users should be able to delete selected restaurant.

### cgi — Common Gateway Interface support
A CGI script is invoked by an HTTP server, usually to process user input submitted through an HTML <FORM> or <ISINDEX> element.



# Developing with frameworks

### Running Flask application

Create menu app using Flask. First I will create basic Flask application:

```python
# Import Flask class from Flask libary
from flask import Flask
# Create instance of the class
# With the name of the running application as argument
app = Flask(__name__)

# Add decorators
@app.route('/')
@app.route('/hello')
def HelloWorld():
    return "Hello World"

# Execute only if file is run by python interpreter
# Can't be imported
if __name__ == '__main__':
    # Enable debug
    app.debug = True
    # Run local server with the application
    app.run(host='0.0.0.0', port=5000)
```

We then use the ``route() decorator`` we tell Flask what URL should trigger our function. The decorator in the above script wraps the function inside the app.route function that was created by Flask. If either of these routes get sent to the browser (``http://localhost:5000/`` or ``http://localhost:5000/hello``) the function HelloWorld will be executed.

The ``run() function`` to run the local server with our application. The if __name__ == '__main__': makes sure the server only runs if the script is executed directly from the Python interpreter and not used as an imported module.

If you enable ``debug support`` the server will reload itself on code changes, and it will also provide you with a helpful debugger if things go wrong. To enable debug support you can use this code:

```python
app.debug = True
app.run()
# or
app.run(debug=True)
```
To stop the server click ```CTRL+C```.


### Adding Database to Flask Application

In order to connect to the database we need to import in out application sqlalchemy modules, create engine and database session. HelloWorld function needs to be updated to be able to query through the restaurant database.


### Routing

The  route decorator is used to bind the function to the URL. To add variable to the URL we can specify the rule:
```
"path/<type: variable_name/path"
```
Type can be integer, string or other path. In our case we can change URL to view certain id of the restaurant:
```python
@app.route('/restaurants/<int:restaurant_id>/')
```

When we create a route for a function it should contain the same number of inputs as the function e.g

```Python
#Create route for editMenuItem function here
@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/edit/')

def editMenuItem(restaurant_id, menu_id):
    return "page to edit a menu item. Task 2 complete!"
```

### Render template

Flask can configure an engine to store html code. To render template you can use code render_template method. All we need to do it is to provide template name and pass variable that HTML template.

This retrieval of data is called ``HTML escaping``.

```python
render_template(templateName.html, variable = keyword)
```

This is example of the HTML template:
```HTML
<html>

<body>

<h1>{{restaurant.name}}</h1>


{% for i in items %}

<div>

<p>{{i.name}}</p>

<p>{{i.description}}</p>

<p> {{i.price}} </p>

</div>


{% endfor %}
</body>

</html>

```

``{%logical code%}`` - logical code that we want to execute from inside of HTML e.g for loop.

``{{printed code}}`` - result printed from html file

``{%endfor%}``, ``{%endif%}`` - indicate end of the statement

Now we can use this template but we need to edit our main piece of code:

```python
@app.route('/restaurants/<int:restaurant_id>/')

def restaurantMenu(restaurant_id):
	restaurant = session.query(Restaurant).first()
	items = session.query(MenuItem).filter_by(restaurant_id = restaurant.id)
  # REMOVE BELOW CODE and replace with render_template

  #output = ''
	#for i in items:
	#	output += i.name
	#	output += '</br>'
	#	output += i.price
	#	output += '</br>'
	#	output += i.description
	#return output

  # Return render_template using menu.html
  # Give escape code access to restaurant and items variables

	return render_template('menu.html', restaurant = restaurant, items = items)

```
### URL Building

It is possible to generate URL using Flask. To build a URL to a specific function you can use the ``url_for() function``.  It accepts the name of the function as first argument and a number of keyword arguments, each corresponding to the variable part of the URL rule. Unknown variable parts are appended to the URL as query parameters.

```python
<a href='{{url_for('editMenuItem', restaurant_id = restaurant.id, menu_id = i.item)}}'>Edit</a>

```
### Form Requests and Redirects

# Iterative Development

 <em>Checklist:</em>
 1. Create mock-ups for every page in the restaurant menu app and design URLs for each page.
 2. Set all routing in your application to be able to navigate to all URLs.
 3. Create all templates and forms.
 4. Add all backend functionality
 5. Add API Endpoints.
 6. Add styling with CSS


# Authentication vs Authorization

### Authentication


# REFERENCES
- https://www.vagrantup.com/docs/networking/forwarded_ports.html
- http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/
- https://docs.python.org/2/library/cgi.html
- http://lepture.com/en/2013/create-oauth-server
- https://pymotw.com/2/BaseHTTPServer/
- https://wiki.python.org/moin/BaseHttpServer
- https://www.safaribooksonline.com/library/view/web-programming-with/9781926873992/
- https://en.wikipedia.org/wiki/HTML#Character_and_entity_references
- http://flask.pocoo.org/docs/0.10/quickstart/#url-building
