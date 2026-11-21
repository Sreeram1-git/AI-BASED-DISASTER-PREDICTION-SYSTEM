def check_weather_risk(weather):

    temperature = weather["temperature"]
    humidity = weather["humidity"]
    rainfall = weather["rainfall"]
    wind_speed = weather["wind_speed"]

    risk = "LOW"

    if rainfall >= 50 or wind_speed >= 60:
        risk = "HIGH"

    elif rainfall >= 20 or wind_speed >= 40:
        risk = "MEDIUM"

    print("\n===== LIVE WEATHER RISK REPORT =====")

    print("Temperature:", temperature, "°C")
    print("Humidity:", humidity, "%")
    print("Rainfall:", rainfall, "mm")
    print("Wind Speed:", wind_speed, "km/h")
    print("Risk Level:", risk)

    print("====================================")

    return risk