import requests
import os
import streamlit as st
import json
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

ET_API_KEY = os.getenv("ET_API_KEY")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

# Define the query parameters for ET
def get_et_args(coordinates):
    return {
        "date_range": ["2020-01-01", "2020-12-31"],
        "interval": "monthly",
        "geometry": coordinates,
        "model": "Ensemble",
        "variable": "ET",
        "reference_et": "gridMET",
        "units": "mm",
        "file_format": "JSON"
    }

# Fetch ET data
def fetch_et_data(coordinates):
    et_args = get_et_args(coordinates)
    response = requests.post(
        headers={"Authorization": ET_API_KEY},
        json=et_args,
        url="https://openet-api.org/raster/timeseries/point"
    )
    if response.status_code == 200:
        return json.loads(response.content)
    else:
        st.error(f"Error fetching ET data: {response.status_code}")
        return None

# Fetch weather data
def fetch_weather_data(location):
    params = {
        "key": WEATHER_API_KEY,
        "q": location,
        "days": 1,
        "aqi": "no",
        "alerts": "no"
    }
    response = requests.get("https://api.weatherapi.com/v1/forecast.json", params=params)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Error fetching weather data: {response.status_code}")
        return None
