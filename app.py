import streamlit as st
from modules.fetch_data import fetch_et_data, fetch_weather_data
from modules.process_data import process_et_data
from modules.visualize_data import visualize_et, plot_weather_forecast
from modules.suggestions import provide_suggestions

def main():
    st.title("NASA Water & Weather Data Tool for Farmers")

    # User input for coordinates and location
    lat = st.number_input("Enter Latitude", value=38.87626)
    lon = st.number_input("Enter Longitude", value=-121.36322)
    location = st.text_input("Enter Location", "San Francisco")

    if st.button("Fetch Data"):
        coordinates = [lon, lat]

        # Fetch ET and weather data
        et_data = fetch_et_data(coordinates)
        weather_data = fetch_weather_data(location)

        if et_data:
            dates, et_values = process_et_data(et_data)
            st.write("### Evapotranspiration Data")
            visualize_et(dates, et_values)

        if weather_data:
            st.write(f"### Weather Data for {location}")
            plot_weather_forecast(weather_data)

        if et_data and weather_data:
            temps = [hour['temp_c'] for hour in weather_data['forecast']['forecastday'][0]['hour']]
            provide_suggestions(et_values, temps)

if __name__ == "__main__":
    main()
