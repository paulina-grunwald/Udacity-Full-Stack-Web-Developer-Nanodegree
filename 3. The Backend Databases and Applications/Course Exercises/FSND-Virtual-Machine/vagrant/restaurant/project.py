# Improt Flask class from Flask libary
from flask import Flask
# Create instance of the class
# With the name of the running application as argument
app = Flask(__name__)


# Import CRUD Operations 
from database_setup import Base, Restaurant, MenuItem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# Create session and connect to DB
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()



# Add decorators
@app.route('/')
@app.route('/hello')
# Envoce HelloWold() function when accessing
# Local host 5000 or localhost 5000/hello
def HelloWorld():
    return "Hello World"

# Execute only if file is run by python interpreter
if __name__ == '__main__':
	# If code change reload
    app.debug = True
    # Run local server with the applicaion
    # Listen on all public addresses
    app.run(host='0.0.0.0', port=5000)