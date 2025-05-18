import requests
import os

YAHOO_FINANCE_API_URL = "https://query1.finance.yahoo.com/v8/finance"

def fetch_stock_data(symbol):
    """Fetch stock data from Yahoo Finance API."""
    url = f"{YAHOO_FINANCE_API_URL}/quote"
    params = {"symbols": symbol}
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def fetch_historical_data(symbol, period='1mo', interval='1d'):
    """Fetch historical stock data from Yahoo Finance API."""
    url = f"{YAHOO_FINANCE_API_URL}/historicaldata"
    params = {
        "symbol": symbol,
        "period": period,
        "interval": interval
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()