# Filename - server.py

# Import flask and datetime module for showing date and time
from flask import Flask, request, jsonify
from flask_cors import CORS  # allows frontend to call backend
import datetime

x = datetime.datetime.now()

# Initializing flask app
app = Flask(__name__)
CORS(app)  # enable cross-origin requests

@app.route('/')
def home():
    return "Peanut butter jelly Peanut butter jelly Peanut butter jelly with a baseball bat"

# test
# Example data
locations = [
    {"id": 1, "name": "UC Berkeley", "lat": 37.8715, "lng": -122.2730},
    {"id": 2, "name": "SF Downtown", "lat": 37.7749, "lng": -122.4194}
]

@app.route('/locations', methods=['GET'])
def get_locations():
    return jsonify(locations)

@app.route('/add_location', methods=['POST'])
def add_location():
    data = request.get_json()
    locations.append(data)
    return jsonify({"message": "Location added", "data": data}), 201

if __name__ == '__main__':
    app.run(debug=True)



# Route for seeing a data
@app.route('/data')
def get_time():

    # Returning an api for showing in  reactjs
    return {
        'Name':"geek", 
        "Age":"22",
        "Date":x, 
        "programming":"python"
        }

# Route for receiving data from frontend... tbd on frontend side
@app.route('/submit_location', methods=['POST'])
def submit_location():
    data = request.get_json()  # Get JSON data from request
    
    # You can access specific fields like:
    name = data.get('latitude')
    email = data.get('longitude')
    
    # Return a response
    return jsonify({
        'message': 'Data received successfully',
        'received': data
    }), 200

# Running app
if __name__ == '__main__':
    app.run(debug=True)