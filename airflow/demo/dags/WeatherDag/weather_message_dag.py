"""
## Print the weather for morning and evening

This DAG gets the weather forecast, builds a message, and pushes xcom
"""
from airflow import Dataset, DAG
from airflow.decorators import task
from pendulum import datetime
import sys
import os
dag_directory = os.path.dirname(os.path.abspath(__file__))
sys.path.append(dag_directory)
sys.path.append(os.path.dirname(__file__))
from airflow.demo.dags.utils import Weather

daily_message_file = Dataset("/tmp/daily_message_file.txt")

with DAG(
    dag_id="weather_message",
    start_date=datetime(2024, 1, 1),
    schedule_interval='@daily',
    catchup=False,
    tags=["WeatherAndStockText"],
):
    @task(outlets=[daily_message_file])
    def get_weather_forecast():
        indy_latitude = 39.791
        indy_longitude = -86.148003

        weather_forecast = Weather.get_weather_forecast(indy_latitude, indy_longitude)
        weather_message = Weather.build_morning_weather_message(weather_forecast)
        with open(daily_message_file.uri, "w") as f:
            f.write(weather_message)

    get_weather_forecast()