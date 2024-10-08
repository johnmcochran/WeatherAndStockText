import requests

#todo: hide api key by using airflow variables
marketstack_api_key = ''


def get_sp500_data():
    url = f"https://api.marketstack.com/v1/eod?access_key={marketstack_api_key}"
    querystring = {"symbols": "SPY", "exchange": "ARCX"}
    sp500_response = requests.get(url, params=querystring).json()
    return sp500_response


def build_sp500_close_price_message(sp500_response):
    sp500close = sp500_response['data'][0]['close']
    close_price_message = f"\nS&P500 Close Price: ${sp500close}"
    return close_price_message
