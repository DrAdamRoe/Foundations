from flask import Flask, jsonify, send_file
from flask_cors import CORS 

app = Flask(__name__)
# enable the api to be accessed by frontend running on localhost
CORS(app, resources={r"/api/*": {"origins": "http://127.0.0.1"}})

# define what to do when the user navigates to "/"
# this serves a static html file. 
@app.route('/')
def index():
    return send_file("static/html/index.html")

# our mock data - like what we could get from a database
restaurants = [
    {'id': 0,
    'name':'Sotto',
    'neighborhood':'Wedding'
    }, 
    {'id': 1,
    'name':'Curry 36',
    'neighborhood':'Kreuzberg'
    }
]

# A HTTP RESTful API Route returning a list of names of restaurants

@app.route('/api/restaurants/names',  methods=['GET'])
def api_restaurants_names():
    # create a new list
    restaurant_names = []
    # loop through the data, adding the names of each restaurant to our new list 
    for restaurant in restaurants: 
        restaurant_names.append(restaurant['name'])
    return jsonify(restaurant_names)



# Run this application if the file is executed, e.g. as "python3 backend.py" 
if __name__ == '__main__': 
    app.testing=True
    app.run()