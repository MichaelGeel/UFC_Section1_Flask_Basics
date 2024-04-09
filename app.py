# First we import the Flask class from flask:
from flask import Flask, jsonify, request

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
# Added the parameter specifying the methods in which this route can be called with.
# Added the name parameter to allow the route to take in data via the url call.
# Adding the default home route decoator above the home route:
@app.route('/home', methods=['GET', 'POST'], defaults={'name': 'Default'})
# Setting the name parameter to be locked as a string data type:
@app.route('/home/<string:name>', methods=['GET', 'POST'])
def home(name):
        return '<h1>Hello {}, you are on the home page!</h1>'.format(name)

# Creating a route to return a jsonified version of python data structures.
@app.route('/json')
def json():
        return jsonify({'key': 'value', 'key2': [1, 2, 3]})

# Creating a new route as an example for query strings:
@app.route('/query')
def query():
        # creating the 2 variables that'll house the query string data.
        name = request.args.get('name')
        location = request.args.get('location')

        # Amending the output to utilize the data we've received.
        return '<h1>Hi {}, you are from {} and are on the query page.</h1>'.format(name, location)

# Creating a new route for lesson 9: Request form data:
@app.route('/theform')
def theform():

        # Creating the form and the relevant inputs to be filled in in the form alongside the submit.
        return '''<form method="POST" action="/process">
                        <input type="text" name="name">
                        <input type="text" name="location">
                        <input type="submit" value="Submit">
                </form>'''

# Adding the process route that will consume the data populated within the theform route:
# Because we're only getting data from the form, this route will only accept post requests.
@app.route('/process', methods=['POST'])
def process():
        # Retrieving the data passed in from the form:
        name = request.form['name']
        location = request.form['location']

        return '<h1>Hello {} from {}. You have submitted the form.</h1>'.format(name, location)

# Route for handling JSON data:
@app.route('/processjson', methods=['POST'])
def processjson():

        # Fetch the json payload sent to this route:
        data = request.get_json()

        # Extracting the data from the payload:
        name = data['name']
        location = data['location']
        rand_list = data['randomlist']

        return jsonify({'result': 'success', 'name': name, 'location': location, 'Rand_list_key': rand_list[2]})

if __name__ == '__main__':
        app.run(debug=True)