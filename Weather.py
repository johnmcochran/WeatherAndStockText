import requests
import json

indy_latitude = 39.791
indy_longitude = -86.148003


def get_weather_forecast(latitude, longitude):
    point_response = requests.get (f'https://api.weather.gov/points/{indy_latitude},{indy_longitude}')
    point = json.loads(point_response.text)
    forecast_url = point["properties"]['forecast']
    forecast_response = requests.get(forecast_url)
    return forecast_response


def build_morning_weather_message(forecast_response):
    afternoon_forecast = json.loads(forecast_response.text)['properties']['periods'][2]
    morning_forecast = json.loads(forecast_response.text)['properties']['periods'][1] #'tonight's temperature really corresponds with temp the following day morning
    weather_message = f"Indy Morning: {morning_forecast['temperature']}F\nIndy Afternoon: {afternoon_forecast['temperature']}F"
    return weather_message

forecast = get_weather_forecast(indy_latitude, indy_longitude)
message = build_morning_weather_message(forecast)
print(message)

