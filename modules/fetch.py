import requests
import pandas as pd
import time
import streamlit as st

API_BASE = "https://api.coingecko.com/api/v3"

@st.cache_data(ttl=300)
def fetch_historical_prices(coin):
    try:
        # Unix timestamps for past 7 days
        now = int(time.time())
        seven_days_ago = now - (7 * 24 * 60 * 60)

        url = f"{API_BASE}/coins/{coin}/market_chart/range"
        params = {
            "vs_currency": "usd",
            "from": seven_days_ago,
            "to": now
        }

        response = requests.get(url)
        data = response.json()

        if "prices" not in data:
            return pd.DataFrame()

        df = pd.DataFrame(data["prices"], columns=["timestamp", "price"])
        df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
        df.set_index("timestamp", inplace=True)
        return df

    except Exception:
        return pd.DataFrame()
