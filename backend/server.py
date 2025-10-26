# Filename - server.py

# Import flask and datetime module for showing date and time
from flask import Flask, request, jsonify
from flask_cors import CORS  # allows frontend to call backend
import datetime

x = datetime.datetime.now()

# Initializing flask app
app = Flask(__name__)

# Allow all routes to be accessed from any origin (development)
CORS(app)

# Route for sending data
@app.route('/api/data')
def output_deals():

    # Letta agent call here...
    # fake_data = {
    # 'name': "Insomnia Cookies",
    # 'lat': 37.8, 
    # 'lng': -122.448,
    # 'deals': [
    #     {
    #         "Deal Type": "Double Dozen Deal",
    #         "Description": "24 Classic Cookies",
    #         "Price/Discount": "$22",
    #         "Availability": "Pickup Only",
    #         "Source": "https://instagram.com"
    #     },
    #     {
    #         "Deal Type": "Cookiewich",
    #         "Description": "Ice Cream Sandwich",
    #         "Price/Discount": "$4",
    #         "Availability": "Pickup Only",
    #         "Source": "https://instagram.com"
    #     },
    #     {
    #         "Deal Type": "Free Cookie On Signup",
    #         "Description": "Free classic cookie on signup",
    #         "Price/Discount": "Free on signup",
    #         "Availability": "Online Order",
    #         "Source": "https://instagram.com"
    #     }]
    # }

    fake_data = [
        {'lat': 37.800000, 'lng': -122.448000},
        {'lat': 37.805000, 'lng': -122.464000},
        {'lat': 37.810000, 'lng': -122.478000},
    ]


    # Returning an api for showing in  reactjs
    return jsonify(fake_data)




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