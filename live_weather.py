
import requests

# ==========================================
# FUNCTION 1: GET LOCATION COORDINATES
# ==========================================

def get_location_coordinates(location):

    url = "https://geocoding-api.open-meteo.com/v1/search"

    params = {
        "name": location,
        "count": 10,
        "language": "en",
        "format": "json"
    }

    try:
        response = requests.get(
            url,
            params=params,
            timeout=15
        )

        response.raise_for_status()

        data = response.json()

        if not data.get("results"):
            print("\nLocation not found. Try another city.")
            return None

        results = data["results"]

        # Display matching locations
        print("\nMatching Locations:")

        for i, place in enumerate(results, start=1):

            city = place.get("name", "Unknown")
            country = place.get("country", "Unknown")
            state = place.get("admin1", "")

            print(f"{i}. {city}, {state}, {country}")

        # Select location
        if len(results) > 1:

            choice = input(
                "\nSelect location number: "
            ).strip()

            if not choice.isdigit():
                print("Invalid selection.")
                return None

            choice = int(choice)

            if choice < 1 or choice > len(results):
                print("Invalid selection.")
                return None

            selected = results[choice - 1]

        else:
            selected = results[0]

        return {
            "latitude": selected["latitude"],
            "longitude": selected["longitude"],
            "city": selected.get("name", "Unknown"),
            "country": selected.get("country", "Unknown")
        }

    except requests.exceptions.RequestException as e:

        print("\nLocation API error:", e)
        return None

# ==========================================
# FUNCTION 2: GET LIVE WEATHER
# ==========================================

def get_live_weather(location=None):

    print("\n===================================")
    print("       WORLDWIDE WEATHER SYSTEM")
    print("===================================")

    # Ask location if not already provided
    if location is None:

        location = input(
            "\nEnter city or location: "
        ).strip()

    if not location:
        print("Please enter a location.")
        return None

    # Get coordinates
    place = get_location_coordinates(location)

    if place is None:
        return None

    latitude = place["latitude"]
    longitude = place["longitude"]

    city = place["city"]
    country = place["country"]

    print(f"\nFetching weather for {city}, {country}...")

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

    try:

        response = requests.get(
            url,
            params=params,
            timeout=15
        )

        response.raise_for_status()

        data = response.json()

        current = data["current"]

        # Extract weather information
        temperature = current["temperature_2m"]
        humidity = current["relative_humidity_2m"]
        rainfall = current["precipitation"]
        wind_speed = current["wind_speed_10m"]

        # Create weather dictionary
        # Both old and new keys are included
        weather = {

            # New keys
            "temperature": temperature,
            "humidity": humidity,
            "rainfall": rainfall,
            "wind_speed": wind_speed,

            # Existing project compatibility
            "temperature_2m": temperature,
            "relative_humidity_2m": humidity,
            "precipitation": rainfall,
            "wind_speed_10m": wind_speed,

            # Location details
            "location": city,
            "country": country,

            # Coordinates
            "latitude": latitude,
            "longitude": longitude
        }

        # Display weather report
        print("\n===================================")
        print("          LIVE WEATHER REPORT")
        print("===================================")

        print(f"Location    : {city}, {country}")
        print(f"Latitude    : {latitude}")
        print(f"Longitude   : {longitude}")

        print("-----------------------------------")

        print(f"Temperature : {temperature} °C")
        print(f"Humidity    : {humidity} %")
        print(f"Rainfall    : {rainfall} mm")
        print(f"Wind Speed  : {wind_speed} km/h")

        print("===================================")

        return weather

    except requests.exceptions.RequestException as e:

        print("\nWeather API error:", e)
        return None

    except (KeyError, ValueError, TypeError) as e:

        print("\nUnable to process weather data:", e)
        return None

# ==========================================
# TEST THE PROGRAM DIRECTLY
# ==========================================

if __name__ == "__main__":

    weather = get_live_weather()

    if weather:

        print("\nWeather data successfully received.")
