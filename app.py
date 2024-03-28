# First we import the Flask class from flask:
from flask import Flask, jsonify


# Instantiating the Flask class that we've imported, __name__ references the name of the module you're working in,
# in this case: app.py
app = Flask(__name__) 

# Creating a route using the Flask object.
# <name> is not html, it's a placeholder.
#Will remove the name placeholder for now.
@app.route('/')# <name>')
# Defining the function tied to the route.
# Added the name parameter to match the <name> placeholder.
def index(): # name):
        # For now we'll just return the below HTML code.
        # Have now added a name variable using the placeholer and format.
        return '<h1>Hello, World!</h1>' # {}!</h1>'.format(name)

# Creating a home route:
@app.route('/home')
def home():
        return '<h1>Hello, you are on the home page!</h1>'

# Creating a route to return a jsonified version of python data structures.
@app.route('/json')
def json():
        return jsonify({'key': 'value', 'key2': [1, 2, 3]})

if __name__ == '__main__':
        app.run()