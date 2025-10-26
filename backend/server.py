# Filename - server.py

# Import flask and datetime module for showing date and time
from flask import Flask, request, jsonify
from flask_cors import CORS  # allows frontend to call backend
import datetime
from PlacesApi import getNearbyRestaurants

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

    nearbyRestaurants = getNearbyRestaurants(data.get("lat"), data.get("lng"))
    if nearbyRestaurants:
        for resta in nearbyRestaurants:
            resta.append("""Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat. In id cursus mi pretium tellus duis convallis. Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.
                            Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat. In id cursus mi pretium tellus duis convallis. Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.
                            Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat. In id cursus mi pretium tellus duis convallis. Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.
                            Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat. In id cursus mi pretium tellus duis convallis. Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.
                            Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat. In id cursus mi pretium tellus duis convallis. Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.
                            Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat. In id cursus mi pretium tellus duis convallis. Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.
                            Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat. In id cursus mi pretium tellus duis convallis. Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.
                            Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat. In id cursus mi pretium tellus duis convallis. Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.
                            Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat. In id cursus mi pretium tellus duis convallis. Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.""")
        

    return jsonify(nearbyRestaurants)

# Running app
if __name__ == '__main__':
    app.run(debug=True)