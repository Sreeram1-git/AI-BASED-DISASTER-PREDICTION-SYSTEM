import csv
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
FILE_PATH = os.path.join(DATA_DIR, "weather_history.csv")

def save_risk_history(weather, risk):
    os.makedirs(DATA_DIR, exist_ok=True)

    file_exists = os.path.exists(FILE_PATH)

    with open(FILE_PATH, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists or os.path.getsize(FILE_PATH) == 0:
            writer.writerow([
                "Date", "Temperature", "Humidity",
                "Rainfall", "Wind Speed", "Risk Level"
            ])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            weather["temperature"],
            weather["humidity"],
            weather["rainfall"],
            weather["wind_speed"],
            risk
        ])