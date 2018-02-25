# Build a Item Catalog Application Project
> by Paulina Grunwald

This project is a part of [Udacity's Full Stack Nanodegree Program](https://www.udacity.com/nanodegree). In this project I had to develop an application that provides a list of items within a variety of categories as well as provide a user registration and authentication system. The goal was also to allow registered users to post, edit and delete their own items. This project combines the knowledge of building dynamic websites with persistent data storage to create a web application that provides a compelling service to the users.


# Table of contents

- [How to run my project](#how-to-run-my-project)
- [Steps taken in developing Item Catalog App](#steps-taken-in-developing-Item-Catalog-App)
- [References](#references)


# How to run my project
In order to be able to run all the files included in this project you need to have installed on your machine following  applications:
- Python 3.6.x
- PostgreSQL 9.6.x
- Vagrant
- VirtualBox

Steps on how to access database:
- Unizp newsdata.rar (you can find newsdata.sql database inside of the zipped file)
- Install Vagrant And VirtualBox
- Clone this repository
- Launch Vagrant VM by running ```vagrant up```, you can the log in with ```vagrant ssh```
- When having problems with starting up your vagrant you can try following command instead vagrant ssh: ```VAGRANT_PREFER_SYSTEM_BIN=1 vagrant ssh```
- To load the data go to the folder where the database is stored, use the command ```psql -d news -f japanesefood.sql``` to connect a database and run the necessary SQL statements.

The database includes three tables:

- The __Category__
- __Dish__


Steps on how to run the application:

1. Install Vagrant and Virtual Box
2. Clone this repository
3. Launch the Vagrant VM
4. From directory /XXX/catalog, initialize the application database by typing python database_setup.py follows by python feedcatalog.py.
5. From directory /XXXX/catalog, run the application within the VM by typing python main.py into the Terminal.
6. Access the application by visiting http://localhost:8000 locally on the browser.

# Tools and Frameworks used

This web application was built using HTML5, CSS, Bootstrap, Vagrant, Flask, SQLAlchemy, Google and Facebook Oauth2 & APIs.

# Steps taken in developing Item Catalog App

The Item Catalog project consists of developing an application that provides a list of items within a variety of categories, as well as provide a user registration and authentication system.

Steps I took to create Catalog App:

1. Create mock-ups for every page in the restaurant menu app and design URLs for each page.
2. Set all routing in your application to be able to navigate to all URLs.
3. Create all templates and forms.
4. Add all backend functionality
5. Add API Endpoints.
6. Add styling with CSS




## 1. Create mock-ups for every

Project structure:
- template folder:
- static folder:


This is the list of requires html templates for various parts of the catalog app:
- index (main page)
- about
- contact
- delete item,
- edit item,
- add image
- edit Image

The HTML is generated using ``Jinja2`` template engine. Base template is a parent to the other pages. I have used template inheritance to create  base template that contains one or more blocks that can be overwriten by it's children by  ``{%extends "base.html"%}``. The blocks are defined by ``{%block content %}..{%endblock%}``.

I also made sure that links are easy to maintain by using jinja2 function ``{{url_for('pagename.htm')}}``.

Maintanable links
Custom Error pages


## 2. Set up routing

Category routing:
- View all categories: /categories/
- Create new category: /category/new
- Edit category: category/<int:category_id>/edit
- Delete category: category/<int:category_id>/edit

Dish routing:
Show all dishes in the category: /category/<int:category_id>/items
Add item to the category: /category/<int:category_id>/items/new


## 4. Add all backend functionality
In  this part of the project i have created two scripts:
- database_setup - this script was used for creating my japanese food database,
- japfood.py - this script was used to insert information about japanese dishes to my previously created japansefood.db

In order to make sure if my database was created correctly



# 6. REFERENCES
- https://tutorial.djangogirls.org/en/template_extending/
- https://en.wikipedia.org/wiki/Tempura
- http://www.japanesecooking101.com/category/by-ingredients/seafood/
- https://app.pluralsight.com/library/courses/flask-micro-framework-introduction/table-of-contents
- https://code.tutsplus.com/tutorials/intro-to-flask-adding-a-contact-page--net-28982
# 7. Image REFERENCES
- https://en.wikipedia.org/wiki/Gy%C5%ABdon#/media/File:Gyuu-don_001.jpg
- https://www.chopstickchronicles.com/yakimeshi-japanese-fried-rice/
- https://www.restaurants-in-hanoi.com/top-restaurants/the-sushi-tokyo.html
- https://images-na.ssl-images-amazon.com/images/I/91YVVQkl4%2BL._SL1500_.jpg
- http://4.bp.blogspot.com/_UIXOn06Pz70/SgTFecsU3hI/AAAAAAAAGzU/NaxCppCjfrY/s800/Okonomiyaki+1+500.jpg
- https://www.japan-talk.com/jt/new/japanese-desserts
