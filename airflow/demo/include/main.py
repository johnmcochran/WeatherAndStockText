
import sys
import os
dag_directory = os.path.dirname(os.path.abspath(__file__))
sys.path.append(dag_directory)
sys.path.append(os.path.dirname(__file__))
import Weather
from airflow.demo.include import Twilio
from airflow.demo.dags.utils import Stocks

indy_latitude = 39.791
indy_longitude = -86.148003

weather_forecast = Weather.get_weather_forecast(indy_latitude, indy_longitude)
weather_message = Weather.build_morning_weather_message(weather_forecast)

sp500_data = Stocks.get_sp500_data()
sp500_message = Stocks.build_sp500_close_price_message(sp500_data)

morning_text_message = weather_message + sp500_message

Twilio.text_message(morning_text_message)