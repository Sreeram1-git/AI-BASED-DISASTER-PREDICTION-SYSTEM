from live_weather import get_live_weather
from risk_analysis import check_weather_risk
from risk_history import save_risk_history
from visualize_risk import visualize_risk
from visualize_weather import visualize_weather
from weather_moniter import weather_monitor
from disaster_risk import (flood_risk,landslide_risk,cyclone_risk,display_risk_report)
from disaster_alert import send_disaster_alert
from weather_history import save_weather_history

def main():

    while True:

        print("\n===================================")
        print(" AI-BASED DISASTER PREDICTION SYSTEM")
        print("===================================")

        print("\nMonitoring Options:")
        print("1. Flood")
        print("2. Landslide")
        print("3. Cyclone")
        print("4. View Live Weather")
        print("5. View Risk History Graph")
        print("6. View Weather History Graph")
        print("7. Continuous Weather Monitoring")
        print("8. Exit")

        choice = input("\nSelect an option (1-8): ")

        if choice == "1":
          weather = get_live_weather()
          if weather:
              result = flood_risk(weather)
              display_risk_report(result)
              send_disaster_alert(
                  result["disaster"],
                  f"{weather['location']}, {weather['country']}",
                  result["risk"]
                  )
            
        elif choice == "2":
            weather = get_live_weather()
            if weather:
                result = landslide_risk(weather)
                display_risk_report(result)
                send_disaster_alert(
                    result["disaster"],
                      f"{weather['location']}, {weather['country']}",
                        result["risk"]
                        )
        elif choice == "3":
            weather = get_live_weather()
            if weather:
                result = cyclone_risk(weather)
                display_risk_report(result)
                send_disaster_alert(
                     result["disaster"],
                       f"{weather['location']}, {weather['country']}",
                       result["risk"])

        elif choice == "4":

            weather = get_live_weather()

            if weather:
                risk = check_weather_risk(weather)
                save_risk_history(weather, risk)
                save_wether_history(weather)
                
        elif choice == "5":
            visualize_risk()

        elif choice == "6":
            visualize_weather()

        elif choice == "7":
            weather_monitor()

        elif choice == "8":
            print("\nThank you for using our system!")
            break

        else:
            print("\nInvalid selection. Please try again.")


if __name__ == "__main__":
    main()