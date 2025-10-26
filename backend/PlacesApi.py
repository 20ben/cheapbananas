import os
import requests
from dotenv import load_dotenv
from datetime import time
import datetime

load_dotenv()

PLACES_API_KEY = os.getenv("GOOGLE_MAPS_API_TOKEN")
if PLACES_API_KEY is None:
    raise ValueError("GOOGLE_MAPS_API_TOKEN not set in .env")

def format_time(hours: int, minutes: int) -> str:
    """Convert 24-hour time to a clean 12-hour format (e.g., 6:00 PM)."""
    t = time(hours, minutes)
    return t.strftime("%-I:%M %p") if minutes else t.strftime("%-I %p")

def get_today_hours(place):
    hours = place.get("currentOpeningHours")
    if not hours:
        return "Hours unavailable"

    weekday_descriptions = hours.get("weekdayDescriptions")
    if not weekday_descriptions:
        return "Hours unavailable"

    # Google starts list at Monday = 0
    today_index = datetime.datetime.today().weekday()
    return weekday_descriptions[today_index]

def get_open_status(place):
    """Return a string like 'Open · Closes 6:00 PM' or 'Closed · Opens 8:00 AM'."""
    hours = place.get("currentOpeningHours")
    if not hours:
        return "Hours unavailable"

    open_now = hours.get("openNow")
    periods = hours.get("periods", [])
    if not periods:
        return "Hours unavailable"

    print(periods)
    # Usually, the first period corresponds to today's schedule
    today = periods[0]
    open_time = today.get("openTime")
    close_time = today.get("closeTime")

    print(close_time)
    print(open_time)

    if not open_time or not close_time:
        return "Hours unavailable"

    open_str = format_time(open_time["hours"], open_time["minutes"])
    close_str = format_time(close_time["hours"], close_time["minutes"])

    if open_now:
        return f"Open · Closes {close_str}"
    else:
        return f"Closed · Opens {open_str}"

def getNearbyRestaurants(latitude, longitude, radius=500.0):

    url = "https://places.googleapis.com/v1/places:searchNearby"

    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": PLACES_API_KEY,
        "X-Goog-FieldMask": "places.displayName,places.formattedAddress,places.location,places.rating,places.currentOpeningHours,places.currentOpeningHours.periods.open,places.currentOpeningHours.periods.close,places.currentOpeningHours.weekdayDescriptions,places.photos,places.primaryTypeDisplayName",
    }

    payload = {
        "includedTypes": ["cafe", "coffee_shop", "dessert_shop", "ice_cream_shop"],
        "maxResultCount": 10,
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
    result = []

    # Filtering.
    places = [p for p in data.get("places", []) if "Hotel" != p.get("primaryTypeDisplayName")["text"]]

    for place in places:
        status = get_today_hours(place)
        photo = place["photos"][0]["name"]
        photo_url = photo_url = f"https://places.googleapis.com/v1/{photo}/media?maxWidthPx=200&key={PLACES_API_KEY}"
        result.append([place["displayName"]["text"], place.get("formattedAddress", "N/A"), place.get("location"), place.get("rating"), status, photo_url, place.get("primaryTypeDisplayName")["text"]])

    return result