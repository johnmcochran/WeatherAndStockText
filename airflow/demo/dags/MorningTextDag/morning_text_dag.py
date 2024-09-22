from airflow import Dataset, DAG
from airflow.decorators import task
from pendulum import datetime
import sys
import os
dag_directory = os.path.dirname(os.path.abspath(__file__))
sys.path.append(dag_directory)
sys.path.append(os.path.dirname(__file__))
sys.path.append('/opt/airflow/demo/dags/utils')
import AWS
import Stocks
import Weather

daily_message_file = Dataset("/tmp/daily_message_file.txt")

with DAG(
    dag_id="WeatherAndStockText",
    start_date=datetime(2024, 1, 1),
    schedule_interval='@daily',
    catchup=False,
    tags=["automate the boring stuff"],
):
    @task(outlets=[daily_message_file])
    def get_weather_forecast():
        indy_latitude = 39.791
        indy_longitude = -86.148003

        weather_forecast = Weather.get_weather_forecast(indy_latitude, indy_longitude)
        weather_message = Weather.build_morning_weather_message(weather_forecast)
        with open(daily_message_file.uri, "w") as f:
            f.write(weather_message)



    # todo: learn how to use timesensor to wait until specific time to execute morning task

    @task(outlets=[daily_message_file])
    def get_stock_close_price():
        sp500_data = Stocks.get_sp500_data()
        sp500_message = Stocks.build_sp500_close_price_message(sp500_data)

        with open(daily_message_file.uri, "a") as f:
            f.write(sp500_message)


    get_weather_forecast() >> get_stock_close_price()

