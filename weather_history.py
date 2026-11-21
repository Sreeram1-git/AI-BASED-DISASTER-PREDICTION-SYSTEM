```python
import csv
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent
DATA_FOLDER = BASE_DIR / "data"
FILE_PATH = DATA_FOLDER / "weather_history.csv"


def save_weather_history(weather):

    DATA_FOLDER.mkdir(parents=True, exist_ok=True)

    file_exists = FILE_PATH.exists()

    with open(FILE_PATH, "a", newline="") as file:

        fieldnames = [
            "Date",
            "Temperature",
            "Humidity",
            "Rainfall",
            "Wind Speed"
        ]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not file_exists or FILE_PATH.stat().st_size == 0:
            writer.writeheader()

        writer.writerow({
            "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Temperature": weather["temperature"],
            "Humidity": weather["humidity"],
            "Rainfall": weather["rainfall"],
            "Wind Speed": weather["wind_speed"]
        })

    print("Weather history saved successfully!")
```