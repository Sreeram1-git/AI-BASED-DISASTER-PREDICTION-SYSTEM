import csv
import os
from datetime import datetime


def save_risk_history(weather, risk):

    os.makedirs("data", exist_ok=True)

    file_path = "data/risk_history.csv"

    file_exists = os.path.exists(file_path)

    with open(file_path, "a", newline="") as file:

        writer = csv.writer(file)

        if not file_exists or os.path.getsize(file_path) == 0:

            writer.writerow([
                "Date",
                "Temperature",
                "Humidity",
                "Rainfall",
                "Wind_Speed",
                "Risk_Level"
            ])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            weather["temperature_2m"],
            weather["relative_humidity_2m"],
            weather["precipitation"],
            weather["wind_speed_10m"],
            risk
        ])

    print("\nRisk history saved successfully!")