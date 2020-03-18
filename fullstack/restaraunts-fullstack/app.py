from flask import Flask, jsonify, send_file
from flask_cors import CORS 

# import function which connects to the database and returns a list of restaurants
from database_connect import get_restaurants_names


app = Flask(__name__)
# enable the api to be accessed by frontend running on localhost
CORS(app, resources={r"/api/*": {"origins": "http://127.0.0.1"}})

# this serves a static html file. 
@app.route('/')
def index():
    return send_file("static/html/index.html")

# an API route to return a JSON Ojbect with restaurant names 
@app.route('/api/restaurants/names',  methods=['GET'])
def api_restaurants_names():
    return jsonify(get_restaurants_names())


# Run this application if the file is executed, e.g. as "python3 backend.py" 
if __name__ == '__main__': 
    app.testing=True
    app.run()
