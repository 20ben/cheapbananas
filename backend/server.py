# Filename - server.py

# Import flask and datetime module for showing date and time
from flask import Flask, request, jsonify
import datetime

x = datetime.datetime.now()

# Initializing flask app
app = Flask(__name__)


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