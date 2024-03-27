# First we import the Flask class from flask:
from flask import Flask


# Instantiating the Flask class that we've imported, __name__ references the name of the module you're working in,
# in this case: app.py
app = Flask(__name__) 

# Creating a route using the Flask object.
# <name> is not html, it's a placeholder.
@app.route('/<name>')
# Defining the function tied to the route.
# Added the name parameter to match the <name> placeholder.
def index(name):
        # For now we'll just return the below HTML code.
        # Have now added a name variable using the placeholer and format.
        return '<h1>Hello {}!</h1>'.format(name)