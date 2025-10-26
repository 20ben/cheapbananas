# Filename - server.py

# Import flask and datetime module for showing date and time
from flask import Flask, request, jsonify
from flask_cors import CORS  # allows frontend to call backend
import datetime

x = datetime.datetime.now()

# Initializing flask app
app = Flask(__name__)


# Route for sending data
@app.route('/data')
def output_deals():

    # Letta agent call here...

    # Returning an api for showing in  reactjs
    return {
        'name':"Insommia Cookies", 
        "Deal":"Cookiewich",
        "Description": "...", 
        "Source":"https://instagram.com/post/postid"
        }

# Route for receiving data from frontend... tbd on frontend side
@app.route('/submit_location', methods=['POST'])
def submit_location():
    data = request.get_json()  # Get JSON data from request
    
    # Process the data (here we just print it)
    print("Received data:", data)

    
    # Return a response
    return jsonify({
        'message': 'Data received successfully',
        'received': data
    }), 200

# Running app
if __name__ == '__main__':
    app.run(debug=True)