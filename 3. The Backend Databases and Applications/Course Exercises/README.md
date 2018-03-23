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

### Message flashing
``Message flashing`` is a feature that will prompt a message to user immediately after certain action has taken place and disappear when the page is requested.

To flash a message within the application we use:
```python
flash("insert message here")
```
To get hold of one of the message we use:
```python
get_flashed_messages()
```

### Responding with JSON

``API`` - Application Programming interface
APIs allow external applications to access public information that our app wants to share.
When an API is communicated over the Internet and following rules of HTTP  it is called ``RESTful API (Representational State Transfer)``. JSON is the mot popular format of sending data using API.

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
Securing your web application:
- strong passwords,
- strong encryption,
- secure communication,
- password storage,
- 2-factor authentication,
- password recovery,
- man-in-the middle attacks

# Creating Google Sign in

In this part of the course I will investigate and build  sin-in into restaurant website using Google's authentication service.
First we need to create client ID and client secret Google to be able to communicate with its API.

1. Go to your app's page in the Google APIs Console — https://console.developers.google.com/apis
2. Create and name the new project
3. Go to Project Dashboard and click on ``APIs&Auth``.
4. Choose Credentials from the menu on the left.
5. Create an OAuth Client ID. Select Web application.
6. Click on ``Configure consent screen``.
7. Click on create client ID and then Edit Settings. Add http://localhost:5000 to ``Authorized Javascript Origins``.

### Create anti forgery state token
Anti-forgery state tokens protect the security of users by preventing anti-forgery attacks. The first step is to create unique session token that your client side code returns.

Now I will add following code to project.py to create unique anti-forgery state token:

```python
# Add new imports
from flask import session as login_session
# Will be used to create random strings
import random, string


# Create anti-forgery state token
@app.route('/login')
def showLogin():
    # create 32 char (digits+letters) random string
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    # store state in loggin_session object under name state
    login_session['state'] = state
    # return login_session state variable
    return "The current session state is %s" % login_session['state']


```

``login_session`` will have a role of dictionary and will store values for the longevity of a user's session with the server.

Now i will create login.html. The file will include the code that goes out to Google to authenticate.

```html
<!DOCTYPE html>
<html>
<head>

  <!--LOAD PRE-REQUISITES FOR GOOGLE SIGN IN -->
  <script src="//ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js"></script>
  <script src="//apis.google.com/js/platform.js?onload=start"> </script>

<!-- END PRE-REQUISITES FOR GOOGLE SIGN IN -->
</head>
<body>
<!-- GOOGLE PLUS SIGN IN BUTTON-->
	<div id="signinButton">
      <span class="g-signin"
        data-scope="openid email"
        data-clientid="568147125453-4c7363gfo7lcvce7ps2o0e3hf3o8bk7m.apps.googleusercontent.com"
        data-redirecturi="postmessage"
        data-accesstype="offline"
        data-cookiepolicy="single_host_origin"
        data-callback="signInCallback"
        data-approvalprompt="force">
      </span>
     </div>
<!--END GOOGLE PLUS SIGN IN BUTTON -->
 </body>
 </html>

```

``data-scope="openid email`` - specifies which google resources we want to access
``data-redirecturi="postmessage"`` - enables one time use code flow
``data-accesstype="offline"``- our server can make requests to Google API even if the user is not logged in.
``data-cookiepolicy="single_host_origin"`` - data-cookiepolicy determines the scope of URIs that can access the cookie. If the website has only one host name we will use single_host_origin.
``data-callback="signInCallback"`` - specified call back function,
``data-approvalprompt="force"`` - user has to log in each time he visits the login age.

Now I will add callback method to handle response that google sends. The google API server provides one-time code to authorize our server and an access token that the clinet can use to make API calls from within the browser.

__Creating GConnect__


Add client_secret.json which includes:
- client_id,
- client secret
- javascript_origins


# Local Permission System

The Local Permission System will leverage the information stored in the login session object and uses sever side logic in the database based on provided credentials. We will make database to store information in a more user specific manner. We need to create table of users and match the data to the specific users. User id column should be added to the Restaurant and Menu Items tables.


| User table           
| ------------- | ------------- |
| email         | string        |
| picture       | string        |
| id            | integer       |
| name          | string        |


Number of modifications have to be done in the database_setup.py and lotsofmenus.py:
- add User table and linked it with user.id Foregin key with Restaurant and MenuItem tables.

```python
class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))
```


- add user to each restaurant and menu item example:

```python
restaurant1 = Restaurant(user_id=1, name="Cocina Y Amor ")

menuItem1 = MenuItem(user_id=1, name="Super Burrito Al Pastor",
                     description="Marinated Pork, Rice, Beans, Avocado, Cilantro, Salsa, Tortilla", price="$5.95", course="Entree", restaurant=restaurant1)
```

Now we need to connect our new User table with back end The back end code will look up the user based on his or her e-mail address.

First let's import ``User Module`` to project.py

Now in project.py we need to create ``createUser function``. It takes login_session as an input and creates new user in the database. It also extracts all the necessary info about the user to create new login (e-mail, picture). At the end it returns new user ID.
```python
def createUser(login_session):
    newUser = User(name=login_session['username'], email=login_session[
                   'email'], picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id

```

Then I added two more functions getUserInfo (which simply returns user object for specific user id) and getUserID (takes as an input e-mail and returns user ID if it exits in the database).

```python
def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None
```

Add additional code piece in gconnect function that will check if user exists and if it doesn't then the new user will be created.

```python
user_id = getUserID(login_session['email'])
  if not user_id:
    user_id = createUser(login_session)
  login_session['user_id'] = user_id
```

# Adding Facebook and other providers

In order to use Facebook OAuth we need to register our app on [Facebook Developers Page](https://developers.facebook.com/). Register your app and Add http://localhost:5000/ to the Valid OAuth. redirect URIs section.

In project folder create fb_client_secrets.json
```json
{
  "web": {
    "app_id": "PASTE_YOUR_APP_ID_HERE",
    "app_secret": "PASTE_YOUR_CLIENT_SECRET_HERE"
  }
}
```
Add client site functionality to login.html. Facebook has two options to perform OAuth login:
- import the Facebook JavaScript (https://developers.facebook.com/docs/facebook-login/web) SDK and use Facebook functions.
- Set up facebook login and add ``http://localhost:5000/`` to the Valid OAuth redirect URIs section.
- construct your OAuth manually.

In this example I will import the Facebook JS SDK. I will add facebook connect and disconnect methods to project.py.

# What's and Why's of APIs
APIs - Application Programming Interface
APIs are responsible for sharing information between two applications.
OSI - Open Interconnection model is built from number of layers:
- application,
- presentation,
- session,
- transport,
- network,
- data link,
- psychical,

SOAP - simple object access protocol
XML -  extensible markup language
JSON - JavaScript Object Notation



# Accessing Published APIs

HTTP is a ``pull protocol`` where the communication is always initiated by the client and the server will respond with the response message.

__HTTP request__ consists of:
1. Header:
  - request line (HTTP Verb, URI, HTTP Version Number) e.g ``GET/home.html/HTTP/1.1``,
  - optional request header (describe specific properties about request): consist of the key value pairs,
2. space (blank line)
3. body (optional): includes additional info

__HTTP response__ may consists of:
1. Header:
  - status line (HTTP version, Status Code, Reason Phase)
2. space (blank line)
3. body (optional): includes additional info


``Query string`` is the part of a uniform resource locator (URL) containing data that does not fit conveniently into a hierarchical path structure. The query string commonly includes fields added to a base URL by a Web browser or other client application, for example as part of an HTML form e.g title=Main_page&action=raw

#### Google Maps API

In next exercise my task was to find long and lat of couple of locations using [Google Maps API](https://developers.google.com/maps/?hl=en) and [Postman](https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop).
After reading Google API documentation I have constructed URL and sent a GET request in Postman:
``https://maps.googleapis.com/maps/api/geocode/json?address=Tokyo,Japan&key=MY_API_KEY``
The result of that request was  json file which included long and lat of Tokyo city in Japan.
```json
{
    "results": [
        {
            "address_components": [
                {
                    "long_name": "Tokyo",
                    "short_name": "Tokyo",
                    "types": [
                        "administrative_area_level_1",
                        "locality",
                        "political"
                    ]
                },
                {
                    "long_name": "Japan",
                    "short_name": "JP",
                    "types": [
                        "country",
                        "political"
                    ]
                }
            ],
            "formatted_address": "Tokyo, Japan",
            "geometry": {
                "bounds": {
                    "northeast": {
                        "lat": 35.8986468,
                        "lng": 153.9876115
                    },
                    "southwest": {
                        "lat": 24.2242626,
                        "lng": 138.942758
                    }
                },
                "location": {
                    "lat": 35.6894875,
                    "lng": 139.6917064
                },
                "location_type": "APPROXIMATE",
                "viewport": {
                    "northeast": {
                        "lat": 35.817813,
                        "lng": 139.910202
                    },
                    "southwest": {
                        "lat": 35.528873,
                        "lng": 139.510574
                    }
                }
            },
            "place_id": "ChIJ51cu8IcbXWARiRtXIothAS4",
            "types": [
                "administrative_area_level_1",
                "locality",
                "political"
            ]
        }
    ],
    "status": "OK"
}

```

#### Forequare APIs

Next exercise consisted of finding venues using Foresquare API using provided lat and long.
```
https://developer.foursquare.com/docs/api/venues/search
```
#### Requesting From Python Code
Now let's create request and response using python:

```Python
import httplib2
import json

def getGeocodeLocation(inputString):
  google_api_key = "PASTE_Your_key"
  locationString = inputString.replace(" ", "+")
  url = ('http://maps.googleapis.com/maps/api/geocode/json?address=%skey=%s'%(locationString,google_api_key))
  h = httplib2.Http()
  response, content = h.request(url, 'GET')
  result = json.loads(content)
  print "response header: %s \n \n" % response
```
The file must be placed in the vagrant directory and vagrant needs to be on. Next we type in the terminal python to start python instance. Once the python instance is on we input:
```python
# import getGeocodeLocation function from geocode.py
from geocode import getGeocodeLocation
# Run getGeocodeLocation function with selected input
getGeocodeLocation("Warsaw, Poland")
```

We get following response:

```http
{u'status': u'OK', u'results': [{u'geometry': {u'location_type': u'APPROXIMATE', u'bounds': {u'northeast': {u'lat': 52.3679992, u'lng': 21.2710984}, u'southwest': {u'lat': 52.0978767, u'lng': 20.8512898}}, u'viewport': {u'northeast': {u'lat': 52.3679992, u'lng': 21.2710984}, u'southwest': {u'lat': 52.0978767, u'lng': 20.8512898}}, u'location': {u'lat': 52.2296756, u'lng': 21.0122287}}, u'address_components': [{u'long_name': u'Warsaw', u'types': [u'locality', u'political'], u'short_name': u'Warsaw'}, {u'long_name': u'Warszawa', u'types': [u'administrative_area_level_2', u'political'], u'short_name': u'Warszawa'}, {u'long_name': u'Masovian Voivodeship', u'types': [u'administrative_area_level_1', u'political'], u'short_name': u'Masovian Voivodeship'}, {u'long_name': u'Poland', u'types': [u'country', u'political'], u'short_name': u'PL'}, {u'long_name': u'05', u'types': [u'postal_code', u'postal_code_prefix'], u'short_name': u'05'}], u'place_id': u'ChIJAZ-GmmbMHkcR_NPqiCq-8HI', u'formatted_address': u'Warsaw, Poland', u'types': [u'locality', u'political']}]}
```

The response includes successful 200 status as well as other metadata.
If we would like to extract only lat and long we need to add following code piece:
```python
latitude = result['results'][0]['geometry']['location']['lat']
longitude = result['results'][0]['geometry']['location']['lng']
return (latitude,longitude)
```

#### Make Your Own API Mashup



# Creating your own API Endpoints



# Securing your API
 Hashing algorithms are one way functions.
Paslib


# Writing Developer-Friendly APIs
If you create new APIs for your app make sure you have good documentation with examples for developers to use and play with them.
URI - uniform Resource Identifier

URI should refer to resources not to the action being performed. It's recommend to use plural form for each resource name.

Error messages sent to users should be short and informative.

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
- http://flask.pocoo.org/docs/0.10/quickstart/
