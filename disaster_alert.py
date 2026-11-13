
def send_disaster_alert(disaster, city, risk_level):
    

    print("\n" + "=" * 45)
    print("          DISASTER ALERT SYSTEM")
    print("=" * 45)

    if risk_level.upper() == "CRITICAL":

        print("!!! CRITICAL RISK ALERT !!!")
        print("Disaster:", disaster)
        print("Location:", city)
        print("Risk Level:", risk_level)

        print("\nSAFETY MESSAGE:")
        print("Follow official emergency instructions.")
        print("Move to a safer location if advised.")

    elif risk_level.upper() == "HIGH":

        print("!!! HIGH RISK ALERT !!!")
        print("Disaster:", disaster)
        print("Location:", city)
        print("Risk Level:", risk_level)

        print("\nSAFETY MESSAGE:")
        print("Stay alert and monitor official warnings.")

    else:
        print("No high-risk alert.")
        print("Current Risk Level:", risk_level)

    print("=" * 45)
send_disaster_alert("flood","kochi","high")