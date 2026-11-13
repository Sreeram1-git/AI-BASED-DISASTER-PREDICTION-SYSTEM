project_name = "Disaster Prediction System"

rainfall = 120
temperature = 28
location = "Kerala"

print(project_name)
print("Rainfall:", rainfall)
print("Temperature:", temperature)
print("Location:", location)

location = input("Enter your location: ")

rainfall = float(input("Enter rainfall in mm: "))

print("Location:", location)
print("Rainfall:", rainfall, "mm")

# If/Else Conditions

rainfall = float(input("Enter rainfall in mm: "))

if rainfall >= 100:
    print("High rainfall recorded")

else:
    print("Rainfall below demonstration threshold")

print("Weather monitoring completed")

# Functions

def check_rainfall(rainfall):

    if rainfall < 50:
        print("Low rainfall")

    elif rainfall <= 100:
        print("Moderate rainfall")

    else:
        print("High rainfall")


# Calling the function

rain = float(input("Enter rainfall in mm: "))

check_rainfall(rain)

# Temperature checking function

def check_temperature(temperature):

    if temperature < 20:
        print("Cool temperature")

    elif temperature <= 30:
        print("Normal temperature")

    else:
        print("High temperature")


# Get temperature from user

temp = float(input("Enter temperature in Celsius: "))

check_temperature(temp)

# Rainfall Monitoring

rainfall_data = [30, 50, 75, 100, 150]

for rainfall in rainfall_data:

    print("Rainfall:", rainfall, "mm")

    if rainfall < 50:
        print("Low rainfall")

    elif rainfall <= 100:
        print("Moderate rainfall")

    else:
        print("High rainfall")

    print("----------------")

weather = {
    "location": "Kerala",
    "rainfall": 120,
    "temperature": 28,
    "humidity": 85
}

print("Location:", weather["location"])
print("Rainfall:", weather["rainfall"], "mm")
print("Temperature:", weather["temperature"], "C")
print("Humidity:", weather["humidity"], "%")

# Weather Data Collection

weather = {}

weather["location"] = input("Enter location: ")

weather["rainfall"] = float(input("Enter rainfall in mm: "))

weather["temperature"] = float(input("Enter temperature in Celsius: "))

weather["humidity"] = float(input("Enter humidity percentage: "))

print("\n----- WEATHER REPORT -----")

print("Location:", weather["location"])
print("Rainfall:", weather["rainfall"], "mm")
print("Temperature:", weather["temperature"], "C")
print("Humidity:", weather["humidity"], "%")
def weather_report(weather):

    print("\n--- WEATHER REPORT ---")

    print("Location:", weather["location"])
    print("Rainfall:", weather["rainfall"])
    print("Temperature:", weather["temperature"])
    print("Humidity:", weather["humidity"])


weather = {
    "location": "Kerala",
    "rainfall": 120,
    "temperature": 28,
    "humidity": 85
}

weather_report(weather)

