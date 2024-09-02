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
import Stocks

daily_message_file = Dataset("/tmp/daily_message_file.txt")

with DAG(
    dag_id="stock_message",
    start_date=datetime(2024, 1, 1),
    schedule_interval='@daily',
    catchup=False,
    tags=["WeatherAndStockText"],
):
    @task(outlets=[daily_message_file])
    def get_stock_close_price():
        sp500_data = Stocks.get_sp500_data()
        sp500_message = Stocks.build_sp500_close_price_message(sp500_data)

        with open(daily_message_file.uri, "a") as f:
            f.write(sp500_message)

    get_stock_close_price()