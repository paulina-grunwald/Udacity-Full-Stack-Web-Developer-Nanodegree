# Improt Flask class from Flask libary
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory
from flask_images import Images
import os

# import CRUD Operations
from database_setup import Base, Category, Dish, User
from sqlalchemy import create_engine, asc, desc
from sqlalchemy.orm import sessionmaker

# Imports necessary for login
from flask import session as login_session
import random, string

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response

import requests

# Create instance of the class
# With the name of the running application as argument (application object)
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'i'
app.secret_key = 'super_secret_key'
images = Images(app)


# Create session and connect to DB
engine = create_engine('sqlite:///japanesefood.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/uploads/<filename>', methods=["GET"])
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


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


# Show catalog page with all the category items
@app.route('/catalog')
def categories():
    categories = session.query(Category).order_by(asc(Category.name))
    items = session.query(Dish).order_by(asc(Dish.name))
    for i in items:
      i.image = i.image.replace("/static/", '')
      print(i.image)
    return render_template('catalog.html', categories=categories, items=items) 
   

# Show all items in the category

@app.route('/catalog/<category_name>/items')
def allCategoryItems(category_name):
  categories = session.query(Category).order_by(asc(Category.name))
  selectedCategory = session.query(Category).filter_by(name=category_name).one()
  items = session.query(Dish).filter_by(category_id=selectedCategory.id).order_by(asc(Dish.name))
  return render_template('catalog.html', categories=categories, selectedCategory=selectedCategory, items=items)



# Show detailed info on selected dish


# Add new category
@app.route('/catalog/addcategory', methods=['GET','POST'])
def addCategory():
  if request.method == 'POST':
    addCategory = Category(name=request.form['name'])
    session.add(addCategory)
    session.commit()
    flash("You've successfully added new category!")
    return redirect(url_for('categories'))
  else:
    return render_template('addCategory.html', )



# Add a new item



# Delete category
@app.route('/catalog/deletecategory', methods=['GET','POST'])
def deleteCategory():
  categories = session.query(Category).order_by(asc(Category.name))
  # Delete category from the database 
  if request.method == 'POST':
    session.delete(categoryToDelete)
    session.commit()
    return redirect(url_for('categories'))
  return render_template('deleteCategory.html', category=categoryToDelete)



# Create routing to the include_del_cat.html code snippet

@app.route('/include', methods=['GET','POST'])
def include_del_cat():

  return render_template('include_del_cat.html')



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


# Add new item to a category

@app.route('/catalog/additem', methods=['GET','POST'])
def addItem():
  categories = session.query(Category).order_by(asc(Category.name))
  if request.method == 'POST':
    itemName = request.form['name']
    itemDescription = request.form['description']
    itemCategory = session.query(Category).filter_by(name=request.form['category']).one()
    itemImage = request.form['image']
    if itemName != '':
      print("item name %s" % itemName)
      addingItem = Dish(name=itemName, description=itemDescription, image=itemImage, category=itemCategory,
                        user_id=itemCategory.user_id)
      session.add(addingItem)
      session.commit()
      return redirect(url_for('categories'))
    else:
      return render_template('addItem.html', categories=categories)
  else:
    return render_template('addItem.html', categories=categories)


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
  port = int(os.environ.get('PORT', 5000))
  app.secret_key = 'super_secret_key'
	# Reload server when code changes
  app.debug = True
	# Run local server with the application
	# Listen on all public addresses
  app.run(host='0.0.0.0', port=5000)
