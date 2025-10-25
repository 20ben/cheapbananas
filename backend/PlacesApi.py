import os
import requests
from dotenv import load_dotenv

load_dotenv()

PLACES_API_KEY = os.getenv("GOOGLE_MAPS_API_TOKEN")
if PLACES_API_KEY is None:
    raise ValueError("GOOGLE_MAPS_API_TOKEN not set in .env")

def main(latitude, longitude, radius=1000.0):

    url = "https://places.googleapis.com/v1/places:searchNearby"

    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": PLACES_API_KEY,
        "X-Goog-FieldMask": "places.displayName,places.formattedAddress",
    }

    payload = {
        "includedTypes": ["restaurant"],
        "maxResultCount": 20,
        "locationRestriction": {
            "circle": {
                "center": {
                    "latitude": latitude,
                    "longitude": longitude,
                },
                "radius": radius,
            }
        },
    }

    response = requests.post(url, headers=headers, json=payload)
    data = response.json()

    if response.status_code != 200:
        print("Error:", response.status_code, data)
        return

    # Adding to dictionary.
    result = {}

    for place in data.get("places", []):
        result[place["displayName"]["text"]] = place.get("formattedAddress", "N/A")

    return result

print(main(37.867359, -122.258377))