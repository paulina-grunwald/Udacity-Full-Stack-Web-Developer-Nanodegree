# Improt Flask class from Flask libary
from flask import Flask, render_template, request, redirect, url_for, flash
# Create instance of the class
# With the name of the running application as argument
app = Flask(__name__)


# import CRUD Operations 
from database_setup import Base, Restaurant, MenuItem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# Create session and connect to DB
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


# add decorators
@app.route('/')
@app.route('/restaurants/<int:restaurant_id>/')

def restaurantMenu(restaurant_id):
	restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
	items = session.query(MenuItem).filter_by(restaurant_id = restaurant.id)
	#output = ''
	#for i in items:
	#	output += i.name
	#	output += '</br>'
	#	output += i.price
	#	output += '</br>'
	#	output += i.description
	#return output
	return render_template('menu.html', restaurant = restaurant, items = items)

#Create route for newMenuItem function here and add GET and POST method
@app.route('/restaurants/<int:restaurant_id>/new/', methods=['GET', 'POST'])

def newMenuItem(restaurant_id):
	if request.method == 'POST':
		newItem = MenuItem(name = request.form['name'], restaurant_id = restaurant_id)
		session.add(newItem)
		session.commit()
		flash("New menu item created!")
		# Redirect user to the main page
		return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
	else:
		return render_template('newmenuItem.html', restaurant_id=restaurant_id)


#Create route for editMenuItem function here
@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/edit',
           methods=['GET', 'POST'])
def editMenuItem(restaurant_id, menu_id):
    editedItem = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedItem.name = request.form['name']
        session.add(editedItem)
        session.commit()
        #flash("Menu item " + editedItem + ' has been edited!' )
        flash("Menu item has been edited!")
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:
        return render_template(
            'editmenuitem.html', restaurant_id=restaurant_id, menu_id=menu_id, item=editedItem)


# Delete Menu Item

#Create route for deleteMenuItem function here and add GET and POST method
@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/delete/', methods=['GET', 'POST'])

def deleteMenuItem(restaurant_id, menu_id):
    deleteItem = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        session.delete(deleteItem)
        session.commit()
        flash("Item has been deleted!")
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:
        return render_template('deletemenuitem.html', item=deleteItem)


# Execute only if file is run by python interpreter
if __name__ == '__main__':
	app.secret_key = 'super_secret_key'
	# Reload server when code changes
	app.debug = True
	# Run local server with the application
	# Listen on all public addresses
	app.run(host='0.0.0.0', port=5000)