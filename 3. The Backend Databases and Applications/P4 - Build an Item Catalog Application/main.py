# Improt Flask class from Flask libary
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash
# Create instance of the class
# With the name of the running application as argument
app = Flask(__name__)

import os

# import CRUD Operations
from database_setup import Base, Category, Dish
from sqlalchemy import create_engine, asc, desc
from sqlalchemy.orm import sessionmaker

# Imports necessary for login
from flask import session as login_session
import random, string


# Create session and connect to DB
engine = create_engine('sqlite:///japanesefood.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()



# Show home page (this is the front page for the application)
@app.route('/')
def home():
    return render_template('home.html')
# Show about page
@app.route('/about')
def about():
    return render_template('about.html')


# Show contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')


# Show catalog page
@app.route('/catalog')
def categories():
    categories = session.query(Category).order_by(asc(Category.name))
    items = session.query(Dish).order_by(asc(Dish.name))
    return render_template('catalog.html', categories=categories, items=items)

# Show all items in the category

@app.route('/catalog/<category_name>/items')
def allCategoryItems(category_name):
    categories = session.query(Category).order_by(asc(Category.name))
    selectedCategory = session.query(Category).filter_by(name=category_name).one()
    items = session.query(Dish).filter_by(category_id=selectedCategory.id).order_by(asc(Dish.name))
    return render_template('catalog.html', categories=categories, selectedCategory=selectedCategory, items=items)

# Add new category
#@app.route('catalog/addcategory', methods=['GET','POST'])
#def addCategory():
#    if request.method == 'POST':
       # addCategory = Category(name=request.form['name'])
       # session.add(addCategory)
        #session.commit()
#        return redirect(url_for('home'))
#    else:
#        return render_template('addCategory.html')


# Delete category
#showCategoryItems
#@app.route('/catalog/deletecategory', methods=['GET','POST'])
#def deleteCategory():

#    if request.method == 'POST':
#        session.delete(categoryToDelete)
#        session.commit()
#        return redirect(url_for('home'))
#    else:
#       return render_template('deleteCategory.html')

# Edit category
#@app.route('/catalog/<category_name>/edit', methods=['GET','POST'])
#def editCategory(category_name):
 #   findCategory = session.quert(Category).filter_by(name=category_name).one() 
 #   if request.method == 'POST':
  #      findCategory.name = request.form['name']
   #     session.delete(categoryToDelete)
    #    session.commit()
     #   return redirect(url_for('home'))
    #else:
     #   return render_template('editCategory.html')


# Add new item to a categoryshowCategoryItems

@app.route('/catalog/additem', methods=['GET','POST'])
def addItem():
    if request.method == 'POST':

        return redirect(url_for('home'))
    else:
        return render_template('addItem.html')


# Delete  item to a category

# Edit  item to a category

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
