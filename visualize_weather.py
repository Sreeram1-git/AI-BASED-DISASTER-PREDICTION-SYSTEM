import csv
import matplotlib.pyplot as plt
from datetime import datetime
import os


def visualize_weather():

    file_path = "data\\weather_history.csv"

    if not os.path.exists(file_path):
        print("Weather history file not found!")
        return

    dates = []
    temperatures = []
    humidities = []
    rainfalls = []
    wind_speeds = []

    with open(file_path, "r", newline="") as file:

        reader = csv.DictReader(file)

        for row in reader:
            dates.append(datetime.strptime(
                row["Date"], "%Y-%m-%d %H:%M:%S"
            ))

            temperatures.append(float(row["Temperature"]))
            humidities.append(float(row["Humidity"]))
            rainfalls.append(float(row["Rainfall"]))
            wind_speeds.append(float(row["Wind Speed"]))

    if not dates:
        print("No weather records available!")
        return

    os.makedirs("graphs", exist_ok=True)

    graph_data = [
        (temperatures, "Temperature History",
         "Temperature (°C)", "temperature_history.png"),

        (humidities, "Humidity History",
         "Humidity (%)", "humidity_history.png"),

        (rainfalls, "Rainfall History",
         "Rainfall (mm)", "rainfall_history.png"),

        (wind_speeds, "Wind Speed History",
         "Wind Speed (km/h)", "wind_speed_history.png")
    ]

    for values, title, ylabel, filename in graph_data:

        plt.figure(figsize=(10, 5))

        plt.plot(dates, values, marker="o")

        plt.title(title)
        plt.xlabel("Date")
        plt.ylabel(ylabel)

        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout()

        plt.savefig("graphs/" + filename)

        print("Saved:", filename)

        plt.show()
        plt.close()


if __name__ == "__main__":
    visualize_weather()