# Filename - server.py

# Import flask and datetime module for showing date and time
from flask import Flask, request, jsonify, Response, stream_with_context
from flask_cors import CORS  # allows frontend to call backend
import datetime
from PlacesApi import getNearbyRestaurants
import time
from LettaManager import LettaManager
import asyncio

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
'''
@app.route('/submit_location_stream', methods=['POST'])
def submit_location_stream():
    """
    Stream restaurant results as they complete
    Uses Server-Sent Events (SSE)
    """
    data = request.get_json()
    lat = data.get("lat")
    lng = data.get("lng")
    
    logger.info(f"Streaming request for lat={lat}, lng={lng}")
    
    def generate():
        """Generator function that yields SSE-formatted data"""
        try:
            # Get nearby restaurants
            nearbyRestaurants = getNearbyRestaurants(lat, lng)
            
            if not nearbyRestaurants:
                yield f"data: {json.dumps({'type': 'error', 'message': 'No restaurants found'})}\n\n"
                return
            
            # Send initial count
            yield f"data: {json.dumps({'type': 'init', 'total': len(nearbyRestaurants)})}\n\n"
            
            # Prepare data for processing
            restaurant_data = [
                {
                    'index': idx,
                    'name': resta[0],
                    'location': resta[1],
                    'raw_data': resta
                }
                for idx, resta in enumerate(nearbyRestaurants[:10])
            ]
            
            # Process and stream results
            for result in process_restaurants_streaming(restaurant_data):
                # Send each result as it completes
                yield f"data: {json.dumps(result)}\n\n"
            
            # Send completion signal
            yield f"data: {json.dumps({'type': 'complete'})}\n\n"
            
        except Exception as e:
            logger.error(f"Streaming error: {str(e)}", exc_info=True)
            yield f"data: {json.dumps({'type': 'error', 'message': str(e)})}\n\n"
    
    return Response(
        stream_with_context(generate()),
        mimetype='text/event-stream',
        headers={
            'Cache-Control': 'no-cache',
            'X-Accel-Buffering': 'no',  # Disable nginx buffering
            'Connection': 'keep-alive'
        }
    )
'''

# Route for receiving data from frontend... tbd on frontend side
@app.route('/submit_location', methods=['POST'])
def submit_location():
    data = request.get_json()  # Get JSON data from request
    
    # Process the data (here we just print it)
    print("Received data:", data)

    results = {}
    nearbyRestaurants = getNearbyRestaurants(data.get("lat"), data.get("lng"))
    if nearbyRestaurants:

        restas = [r[:2] for r in nearbyRestaurants]
        
        manager = LettaManager()
        result = asyncio.run(manager.process_restaurants(restas))
        results.update(result)
    
    print(results)

    return jsonify(results)


        

    return jsonify(nearbyRestaurants)

# Running app
if __name__ == '__main__':
    app.run(debug=True)