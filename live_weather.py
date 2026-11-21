import requests


# GET LOCATION COORDINATES
def get_location_coordinates(location):

    url = "https://geocoding-api.open-meteo.com/v1/search"

    params = {
        "name": location,
        "count": 10,
        "language": "en",
        "format": "json"
    }

    response = requests.get(url, params=params, timeout=15)
    response.raise_for_status()

    data = response.json()

    if not data.get("results"):
        raise ValueError("Location not found")

    # Select the first matching result for now
    selected = data["results"][0]

    return {
        "latitude": selected["latitude"],
        "longitude": selected["longitude"],
        "city": selected.get("name", "Unknown"),
        "country": selected.get("country", "Unknown")
    }


# GET LIVE WEATHER
def get_live_weather(location):

    if not location or not location.strip():
        raise ValueError("Please enter a location")

    # Get location details
    place = get_location_coordinates(location.strip())

    latitude = place["latitude"]
    longitude = place["longitude"]

    # Weather API
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": [
            "temperature_2m",
            "relative_humidity_2m",
            "precipitation",
            "wind_speed_10m"
        ],
        "timezone": "auto"
    }

    response = requests.get(url, params=params, timeout=15)
    response.raise_for_status()

    data = response.json()
    current = data["current"]

    weather = {
        "temperature": current["temperature_2m"],
        "humidity": current["relative_humidity_2m"],
        "rainfall": current["precipitation"],
        "wind_speed": current["wind_speed_10m"],

        "location": place["city"],
        "country": place["country"],

        "latitude": latitude,
        "longitude": longitude
    }

    return weather


# TEST
if __name__ == "__main__":

    weather = get_live_weather("Kottayam")

    print(weather)