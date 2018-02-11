# Improt Flask class from Flask libary
from flask import Flask
# Create instance of the class
# With the name of the running application as argument
app = Flask(__name__)


# add decorators
@app.route('/')
@app.route('/hello')
def HelloWorld():
    return "Hello World"

# Execute only if file is run by python interpreter
if __name__ == '__main__':
    app.debug = True
    # Run local server with the applicaion
    app.run(host='0.0.0.0', port=5000)