import streamlit as st
import pandas as pd
from modules.fetch import fetch_current_prices, fetch_historical_prices
from modules.charts import plot_price_chart
from modules.forecast import forecast_price

st.set_page_config(page_title="CryptoWatch-AI", page_icon="🚀", layout="wide")

st.title("🪙 CryptoWatch-AI — Real-Time Crypto Insights")

coins = ["bitcoin", "ethereum", "tether", "dogecoin"]

selected_coin = st.selectbox("Select Cryptocurrency", coins)

# Fetch current price
current_price = fetch_current_prices(selected_coin)
st.metric(label=f"{selected_coin.upper()} Price (USD)", value=f"${current_price:,.2f}")

# Fetch historical data
history_df = fetch_historical_prices(selected_coin)

st.subheader("📈 Last 7 Days Trend")
st.line_chart(history_df["price"])

# Forecast feature
st.subheader("🔮 Price Prediction")
future_df = forecast_price(history_df["price"])
st.line_chart(future_df)
