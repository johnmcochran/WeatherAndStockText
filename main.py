import Stocks, Twilio, Weather

indy_latitude = 39.791
indy_longitude = -86.148003

weather_forecast = Weather.get_weather_forecast(indy_latitude, indy_longitude)
weather_message = Weather.build_morning_weather_message(weather_forecast)

sp500_data = Stocks.get_sp500_data()
sp500_message = Stocks.build_sp500_close_price_message(sp500_data)

morning_text_message = weather_message + sp500_message

Twilio.text_message(morning_text_message)