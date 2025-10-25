import requests
import json
import os
from dotenv import load_dotenv

# load Letta API key from from .env and check validity
load_dotenv()
PLACES_API_KEY = os.environ.get('GOOGLE_MAPS_API_TOKEN')
if PLACES_API_KEY is None:
    raise ValueError("GOOGLE_MAPS_API_TOKEN environment variable not set")

# Google Maps API. Given a latitude and longitude (and optionally, radius in miles),
#   return an dictionary of place names to their locations.
def main(latitude: int, longitude: int, radius: int = 5):

    print(PLACES_API_KEY)


main(0, 0)

