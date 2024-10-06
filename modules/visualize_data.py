import matplotlib.pyplot as plt
import plotly.graph_objects as go
import streamlit as st

# Visualize ET data
def visualize_et(dates, et_values):
    # Matplotlib plot (static visualization)
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(dates, et_values, marker='o', linestyle='-', color='b')
    ax.set_title("Monthly Evapotranspiration (ET) Over Time")
    ax.set_xlabel("Date")
    ax.set_ylabel("Evapotranspiration (mm)")
    ax.tick_params(axis='x', rotation=45)
    st.pyplot(fig)

# Plot weather forecast
def plot_weather_forecast(weather_data):
    forecast = weather_data['forecast']['forecastday'][0]['hour']
    times, temps = [], []
    for hour_data in forecast:
        times.append(hour_data['time'])
        temps.append(hour_data['temp_c'])

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(times, temps, marker='o')
    ax.set_title(f"Hourly Temperature Forecast")
    ax.set_xlabel('Time')
    ax.set_ylabel('Temperature (°C)')
    ax.tick_params(axis='x', rotation=45)
    st.pyplot(fig)
