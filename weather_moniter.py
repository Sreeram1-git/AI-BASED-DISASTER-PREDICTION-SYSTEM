import time

from live_weather import get_live_weather
from risk_analysis import check_weather_risk
from risk_history import save_risk_history


def weather_monitor():

    print("\n===================================")
    print("   WORLDWIDE WEATHER MONITORING")
    print("===================================")

    # Ask for location only once
    location = input("\nEnter city or location: ").strip()

    if not location:
        print("Invalid location.")
        return

    print(f"\nMonitoring location: {location}")

    try:

        while True:

            print("\n===================================")
            print("       CHECKING WEATHER")
            print("===================================")

            # Fetch weather for the selected location
            weather = get_live_weather(location)

            if weather:

                print("\nWeather data received successfully!")

                # Analyse disaster risk
                risk = check_weather_risk(weather)

                print("\nFinal Risk Status:", risk)

                # Save risk history
                save_risk_history(weather, risk)

                print("\nRisk history saved successfully!")

            else:

                print("\nUnable to fetch weather data.")
                print("Will try again after 60 seconds.")

            print("\nNext weather update in 60 seconds...")

            time.sleep(60)

    except KeyboardInterrupt:

        print("\n\n===================================")
        print("   WEATHER MONITORING STOPPED")
        print("===================================")

        print("Thank you for using our system!")


if __name__ == "__main__":

    weather_monitor()