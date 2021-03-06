# Retrieve weather information from Open Weather using latitude and longitude to obtain location

import requests
import os

LATITUDE = 36.750671
LONGITUDE = -95.944389

OWM_API_KEY = os.environ['OWM_API']
WEATHER_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"

weather_parameters = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": OWM_API_KEY,
    "units": "imperial",
    "exclude": "minutely,hourly,alerts"

}


def daily_temperature():
    """Obtain temperature readings for current day"""
    response = requests.get(WEATHER_ENDPOINT, params=weather_parameters)
    response.raise_for_status()
    weather_data = response.json()
    current_temperature = weather_data['current']['temp']
    current_condition = weather_data['current']['weather'][0]['description']
    feels_like = weather_data['current']['feels_like']
    max_temperature = weather_data['daily'][0]['temp']['max']
    min_temperature = weather_data['daily'][0]['temp']['min']
    return current_temperature, feels_like, max_temperature, min_temperature, current_condition



