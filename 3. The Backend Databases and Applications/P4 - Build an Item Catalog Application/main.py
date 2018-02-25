# Improt Flask class from Flask libary
from flask import Flask, render_template, request, redirect, url_for, flash
# Create instance of the class
# With the name of the running application as argument
app = Flask(__name__)

import os

# import CRUD Operations 
from database_setup import Base, Category, Dish
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# Create session and connect to DB
engine = create_engine('sqlite:///japanesefood.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


# Show home page
@app.route('/')
@app.route('/catalog')
def home():
    #categories = session.query(Category).order_by(asc(Category.name))
    #items = session.query(Dish).order_by(desc(Dish.name))
    #if 'username' not in login_session:
    #return render_template('index.html', categories=categories, items=items)
    return render_template('index.html')
    #else:
        #return render_template('home.html', categories=categories, items=items)

# Show all items in a category

# Add a new category

# Edit a category

# Add an item 

# Edit an item

# Show about page

@app.route('/about')
def about():
  
    return render_template('about.html')


# Show contact page

@app.route('/contact')
def contact():
 
    return render_template('contact.html')

# Show catalog page

@app.route('/categories')
def categories():
 
    return render_template('categories.html')


# Add routing to error 404 and 505 pages

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500



# Execute only if file is run by python interpreter
if __name__ == '__main__':
	app.secret_key = 'super_secret_key'
	# Reload server when code changes
	app.debug = True
	# Run local server with the application
	# Listen on all public addresses
	app.run(host='0.0.0.0', port=5000)