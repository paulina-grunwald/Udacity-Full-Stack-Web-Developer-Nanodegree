# Build a Item Catalog Application Project
> by Paulina Grunwald

This project is a part of [Udacity's Full Stack Nanodegree Program](https://www.udacity.com/nanodegree). In this project I had to develop an application that provides a list of items within a variety of categories as well as a user registration and authentication system using OAuth. The goal was also to allow registered users to post, edit and delete their own items. This project combines the knowledge of building dynamic websites with persistent data storage to create a web application that provides a compelling service to the users.


# Table of contents

- [How to run my project](#how-to-run-my-project)
- [Tools and Frameworks used](#tools-and-frameworks-used)
- [Steps taken in developing Item Catalog App](#steps-taken-in-developing-Item-Catalog-App)
- [Reflections and learning after finishing the project](#reflections-and-learnings)
- [References](#references)


# How to run my project
In order to be able to run all the files included in this project you need to have installed on your machine following  applications:
- Python 3.6.x
- PostgreSQL 9.6.x
- Vagrant
- VirtualBox

###### Steps for running Japanese Food Catalog App:

1. Install Vagrant and Virtual Box.
2. Clone this repository.
3. Launch the Vagrant VM (by typing vagrant up in the directory /P4 - Build an Item Catalog Application from the terminal).
4. If you would like to recreated already provided japfood.db you can need to run two python in terminal by typing ``python database_setup.py`` and then ``python japfood.py``.
5. Launch Vagrant VM by running ```vagrant up```, you can the log in with ```vagrant ssh``` (When having problems with starting up your vagrant you can try following command instead vagrant ssh: ```VAGRANT_PREFER_SYSTEM_BIN=1 vagrant ssh```).
6. From directory inside of the project directory, run the Japanese Catalog app within the VM by typing `python main.py` into the terminal.  
7. You can access locally the app by going to typing http://localhost:8000 in the browser.

<em>Note</em>: Use following code in terminal (when connected to vagrant) ```psql -d news -f japanesefood.sql``` to connect a database and run the SQL statements if required.

__Project structure__:
- template folder: contains all html pages that build Japanese Food Catalog App.
- static folder:
  - css: contains all stylesheets
  - img: contains all images used on the website
  - js: contaisn all js scripts.



###### Live version of this project is available at: !!!!to be filled!!!!

# Tools and Frameworks used

This web application was built using HTML5, CSS, Bootstrap4, Vagrant, Flask, SQLAlchemy, Google and Facebook Oauth2 & APIs.

# Steps taken in developing Item Catalog App

The Item Catalog project consists of developing an application that provides a list of items within a variety of categories, as well as provide a user registration and authentication system. In this project I have used Flask framework.

Steps I took to create Catalog App:

1. Create mock-ups for every page in the restaurant menu app and design URLs for each page.
2. Set all routing in your application to be able to navigate to all URLs.
3. Create all templates and forms.
4. Add all backend functionality
5. Add API Endpoints.
6. Create authentication&Authorization
7. Add styling with CSS

## 1. Create mock-ups for every
The first step I took was to create mock-ups for each page in my application. This is the list of requires html templates for various parts of the catalog app:
- home (main page)
- about,
- contact,
- add category,
- delete category ,
- edit category,
- add item,
- delete item,
- edit item,
- edit Image
- delete Image

The HTML is generated using ``Jinja2`` template engine. Base template is a parent to the other pages. I have used template inheritance to create  base template that contains one or more blocks that can be overwritten by it's children by  ``{%extends "base.html"%}``. The blocks are defined by ``{%block content %}..{%endblock%}``.

I also made sure that links are easy to maintain by using jinja2 function ``{{url_for('pagename.htm')}}``.

Custom Error pages for 404 and 500 error were created.

## 2. Set up routing


Routing to a home page: ``'/'``
Routing to about page: ``'/about'``
Routing to contact page: ``'/contact'``

Category routing:
- View all categories: ``'/catalog'``
- View all items from selected category: ``/catalog/<category_name>/items``
- Create new category: ``/catalog/addcategory``
- Edit category: category: ``/<int:category_id>/edit``
- Delete category: ``category/<int:category_id>/delete``

Dish routing:
Show all dishes in the category: /category/<int:category_id>/items
Add item to the category: ``'/catalog/additem'``

Error handlers:
```python
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

```

Now I will add API Endpoints to my applications. The API request should return a JSON object for a list of categories, category items, all users, info of specific item. e.g
```python
# add API endpoints for all categories
@app.route('/categories/json')
def categoriesJSON():
  categories = session.query(Category).all()
  return jsonify(Categories = [c.serialize for c in categories])
```
Result of accessing ``http://localhost:5000/categories/json``:
```
{
  "Categories": [
    {
      "id": 1,
      "name": "Rice Dishes",
      "user_id": 1
    },
    {
      "id": 2,
      "name": "Seafood Dishes",
      "user_id": 1
[...]
```
## 4. Add all backend functionality
In  this part of the project I have created two scripts:
1. ``database_setup.py`` - this script was used for creating my Japanese food database. It created the database that contains two tables:
- Category (contains id, name and relationship to Dish table)
- Dish (contains id, description, created date, image, category_id and relationship to Category table)

2. ``japfood.py`` - this script was used to insert information about Japanese dishes to my previously created japansefood.db. Below you can find code example for adding one dish to first catefory:

```python
category1 = Category(name="Rice Dishes")

session.add(category1)
session.commit()

item1 = Dish(name="Donburi", description="Donburi refers to a bowl of plain cooked rice with some other food on top of it. Donburi are served at specialty restaurants, but they are also a common dish that can be found on all kinds of restaurants' menus. Some of the most popular varieties are gyudon (stewed beef), katsudon (tonkatsu), tendon (tempura), oyakodon (chicken and egg), tekkadon (maguro), and kaisendon (raw seafood).",
                     image="/static/img/donburi.jpg", category=category1)
```

3. ``session.py`` - this script was used only in order to make sure that  my database japanesefood.db was created successfuly and items from japfood.py  loaded to the japanesefood.db. I have copied this script in the terminal after launching vagrant in my project directory.

4. ``main.py`` - this is main file for the project. In essence provides web in Python that uses database to implement CRUD. In consists of following sections:
- Import all of the modules

- Create session and connect to DB
- routing to all the pages.

To make sure that all links are Maintanable ``url_for(view)`` function was used. It generatres URL to the given view and it is available in the template contex.




In this project I have used Flask framework.

6. Create authentication&Authorization

Create Google Sign in:



gconnect route responds to POST request. It accepts the authorization code from client, exchanges it for an access token, uses makes an API call to Oauth server and responds to the client.
 Page login

Public pages:

The users will be able to delete, edit, add category and dish items only when logged in.

# Reflections and learning after finishing the project

# REFERENCES
- https://tutorial.djangogirls.org/en/template_extending/
- https://en.wikipedia.org/wiki/Tempura
- http://www.japanesecooking101.com/category/by-ingredients/seafood/
- https://app.pluralsight.com/library/courses/flask-micro-framework-introduction/table-of-contents
- https://code.tutsplus.com/tutorials/intro-to-flask-adding-a-contact-page--net-28982
- https://stackoverflow.com/questions/6654958/make-body-have-100-of-the-browser-height
- http://nipponcolors.com/
- https://en.wikipedia.org/wiki/Japanese_cuisine
- https://app.pluralsight.com/library/courses/responsive-web-design-media-queries-css-preprocessing/table-of-contents
# 7. Image REFERENCES
- https://en.wikipedia.org/wiki/Gy%C5%ABdon#/media/File:Gyuu-don_001.jpg
- https://www.chopstickchronicles.com/yakimeshi-japanese-fried-rice/
- https://www.restaurants-in-hanoi.com/top-restaurants/the-sushi-tokyo.html
- https://images-na.ssl-images-amazon.com/images/I/91YVVQkl4%2BL._SL1500_.jpg
- http://4.bp.blogspot.com/_UIXOn06Pz70/SgTFecsU3hI/AAAAAAAAGzU/NaxCppCjfrY/s800/Okonomiyaki+1+500.jpg
- https://www.japan-talk.com/jt/new/japanese-desserts
- http://sites.dartmouth.edu/folklorearchive/files/2016/11/japan.jpg
