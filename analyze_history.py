import pandas as pd

# Read historical weather data
data = pd.read_csv("weather_history.csv")

# Display all weather records
print("\n--- Historical Weather Data ---")
print(data)

# Calculate average temperature
average_temp = data["Temperature"].mean()

# Find maximum temperature
max_temp = data["Temperature"].max()

# Find minimum temperature
min_temp = data["Temperature"].min()

# Calculate average humidity
average_humidity = data["Humidity"].mean()

# Calculate average rainfall
average_rainfall = data["Rainfall"].mean()

# Display analysis
print("\n--- Weather Analysis Report ---")

print("Average Temperature:", round(average_temp, 2))
print("Maximum Temperature:", max_temp)
print("Minimum Temperature:", min_temp)
print("Average Humidity:", round(average_humidity, 2))
print("Average Rainfall:", round(average_rainfall, 2))