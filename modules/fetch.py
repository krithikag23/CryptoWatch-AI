import requests
import pandas as pd
import time
import streamlit as st

API_BASE = "https://api.coingecko.com/api/v3"

HEADERS = {
    "accept": "application/json",
    "User-Agent": "Mozilla/5.0"
}

@st.cache_data(ttl=60)
def fetch_current_price(coin):
    try:
        url = f"{API_BASE}/simple/price"
        params = {"ids": coin, "vs_currencies": "usd"}
        response = requests.get(url, params=params, headers=HEADERS)

        print("Current Price Status:", response.status_code)
        print(response.text[:200])

        data = response.json()
        return data[coin]["usd"]
    except:
        return None


@st.cache_data(ttl=300)
def fetch_historical_prices(coin):
    try:
        now = int(time.time())
        seven_days_ago = now - (7 * 24 * 60 * 60)

        url = f"{API_BASE}/coins/{coin}/market_chart/range"
        params = {
            "vs_currency": "usd",
            "from": seven_days_ago,
            "to": now
        }

        response = requests.get(url, params=params, headers=HEADERS)

        print("History Status:", response.status_code)
        print(response.text[:200])

        data = response.json()

        if "prices" not in data:
            return pd.DataFrame()

        df = pd.DataFrame(data["prices"], columns=["timestamp", "price"])
        df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
        df.set_index("timestamp", inplace=True)
        return df

    except Exception as e:
        print("Error:", e)
        return pd.DataFrame()
