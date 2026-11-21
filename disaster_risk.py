


def get_weather_values(weather):

    temperature = weather.get(
        "temperature",
        weather.get("temperature_2m", 0)
    )

    humidity = weather.get(
        "humidity",
        weather.get("relative_humidity_2m", 0)
    )

    rainfall = weather.get(
        "rainfall",
        weather.get("precipitation", 0)
    )

    wind_speed = weather.get(
        "wind_speed",
        weather.get("wind_speed_10m", 0)
    )

    return temperature, humidity, rainfall, wind_speed



def get_risk_level(score):

    if score >= 70:
        return "HIGH"

    elif score >= 40:
        return "MODERATE"

    else:
        return "LOW"


def flood_risk(weather):

    _, _, rainfall, _ = get_weather_values(weather)

    score = 0

    if rainfall >= 10:
        score += 70

    elif rainfall >= 5:
        score += 45

    elif rainfall >= 2:
        score += 20

    risk = get_risk_level(score)

    return {
        "disaster": "Flood",
        "score": score,
        "risk": risk
    }


def landslide_risk(weather):

    _, _, rainfall, _ = get_weather_values(weather)

    score = 0

    if rainfall >= 10:
        score += 70

    elif rainfall >= 5:
        score += 45

    elif rainfall >= 2:
        score += 20

    risk = get_risk_level(score)

    return {
        "disaster": "Landslide",
        "score": score,
        "risk": risk
    }
def cyclone_risk(weather):

    _, _, _, wind_speed = get_weather_values(weather)

    score = 0

    if wind_speed >= 60:
        score = 70

    elif wind_speed >= 40:
        score = 45

    elif wind_speed >= 25:
        score = 20

    risk = get_risk_level(score)

    return {
        "disaster": "Cyclone",
        "score": score,
        "risk": risk
    }


def display_risk_report(result):

    print("\n===================================")
    print("       DISASTER RISK REPORT")
    print("===================================")

    print("Disaster:", result["disaster"])

    print("Risk Score:", result["score"], "/ 100")

    print("Risk Level:", result["risk"])

    print("===================================")

    print("\nNote: Educational weather screening only.")

    print("This is not an official disaster warning.")

# ==========================================
# TESTING
# ==========================================

if __name__ == "__main__":

    sample_weather = {
        "temperature": 30,
        "humidity": 85,
        "rainfall": 12,
        "wind_speed": 20
    }

    print("\nTESTING FLOOD RISK")
    display_risk_report(flood_risk(sample_weather))

    print("\nTESTING LANDSLIDE RISK")
    display_risk_report(landslide_risk(sample_weather))

    print("\nTESTING CYCLONE RISK")
    display_risk_report(cyclone_risk(sample_weather))