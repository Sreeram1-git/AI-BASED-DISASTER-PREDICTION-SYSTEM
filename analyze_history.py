import pandas as pd
data = pd.read_csv("weather_history.csv")


print("\n--- Historical Weather Data ---")
print(data)


average_temp = data["Temperature"].mean()


max_temp = data["Temperature"].max()


min_temp = data["Temperature"].min()


average_humidity = data["Humidity"].mean()


average_rainfall = data["Rainfall"].mean()


print("\n--- Weather Analysis Report ---")

print("Average Temperature:", round(average_temp, 2))
print("Maximum Temperature:", max_temp)
print("Minimum Temperature:", min_temp)
print("Average Humidity:", round(average_humidity, 2))
print("Average Rainfall:", round(average_rainfall, 2))