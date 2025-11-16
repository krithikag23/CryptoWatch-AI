import requests
import pandas as pd
from datetime import datetime
import streamlit as st

API_BASE = "https://api.coingecko.com/api/v3"

@st.cache_data(ttl=60)  # Reduce rate limits
def fetch_current_price(coin):
    try:
        url = f"{API_BASE}/simple/price?ids={coin}&vs_currencies=usd"
        response = requests.get(url).json()
        return response[coin]["usd"]
    except:
        return None


@st.cache_data(ttl=300)
def fetch_historical_prices(coin):
    url = f"{API_BASE}/coins/{coin}/market_chart"
    params = {"vs_currency": "usd", "days": 7}
    
    response = requests.get(url)

    if response.status_code != 200:
        return pd.DataFrame()

    data = response.json()

    if "prices" not in data:
        return pd.DataFrame()

    df = pd.DataFrame(data["prices"], columns=["timestamp", "price"])
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
    df.set_index("timestamp", inplace=True)
    return df
