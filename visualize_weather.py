import csv
import matplotlib.pyplot as plt
from datetime import datetime
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

def visualize_weather():

    file_path = BASE_DIR / "data" / "weather_history.csv"
    print("Python is checking:", file_path)
    print("File exists:", file_path.exists())
    graph_folder = BASE_DIR / "static" / "graphs"

    if not file_path.exists():
        print("Weather history file not found!")
        return []

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
        return []

    graph_folder.mkdir(parents=True, exist_ok=True)

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

    graph_urls = []

    for values, title, ylabel, filename in graph_data:

        plt.figure(figsize=(10, 5))

        plt.plot(dates, values, marker="o")

        plt.title(title)
        plt.xlabel("Date")
        plt.ylabel(ylabel)

        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout()

        save_path = graph_folder / filename
        plt.savefig(save_path)

        plt.close()

        graph_urls.append("/static/graphs/" + filename)

        print("Saved:", save_path)

    return graph_urls


if __name__ == "__main__":
    visualize_weather()