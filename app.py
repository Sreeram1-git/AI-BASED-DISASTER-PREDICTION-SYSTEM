from flask import Flask, render_template, request, jsonify

import os

from live_weather import get_live_weather
from risk_analysis import check_weather_risk
from disaster_risk import (
    flood_risk,
    landslide_risk,
    cyclone_risk
)

app = Flask(__name__)


# HOME PAGE
@app.route("/")
def home():
    return render_template("index.html")


# GENERATE WEATHER HISTORY GRAPHS
@app.route("/generate_weather_graphs")
def generate_weather_graphs():

    try:
        graph_urls = visualize_weather()

        if not graph_urls:
            return jsonify({
                "error": "No weather history available. Search for a city first."
            }), 404

        return jsonify({
            "graphs": graph_urls
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


# LIVE WEATHER AND DISASTER RISK
@app.route("/get_weather")
def weather():

    city = request.args.get("city", "").strip()

    if not city:
        return jsonify({
            "error": "Please enter a city name"
        }), 400

    try:

        weather_data = get_live_weather(city)
        save_weather_history(weather_data)

        # Overall weather risk
        risk = check_weather_risk(weather_data)

        # Individual disaster risks
        flood = flood_risk(weather_data)
        landslide = landslide_risk(weather_data)
        cyclone = cyclone_risk(weather_data)

        weather_data["overall_risk"] = risk

        weather_data["disaster_risks"] = {
            "flood": flood,
            "landslide": landslide,
            "cyclone": cyclone
        }

        return jsonify(weather_data)

    except ValueError as e:

        return jsonify({
            "error": str(e)
        }), 404

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


# RUN FLASK APPLICATION
if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=False
    )