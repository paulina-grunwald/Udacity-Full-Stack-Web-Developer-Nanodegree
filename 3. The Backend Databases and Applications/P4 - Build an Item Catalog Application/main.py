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
@app.route('/catalog')
def showHome():
    categories = session.query(Category).order_by(asc(Category.name))
    items = session.query(Dish).order_by(desc(Dish.createdDate))
    #if 'username' not in login_session:
        return render_template('home.html', categories=categories, items=items)
    #else:
        #return render_template('home.html', categories=categories, items=items)

# Show all items in a category

# Add a new category

# Edit a category

# Add an item 

# Edit an item

# Execute only if file is run by python interpreter
if __name__ == '__main__':
	app.secret_key = 'super_secret_key'
	# Reload server when code changes
	app.debug = True
	# Run local server with the application
	# Listen on all public addresses
	app.run(host='0.0.0.0', port=5000)