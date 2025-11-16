import streamlit as st
import pandas as pd
from modules.fetch import fetch_current_price, fetch_historical_prices
from modules.forecast import forecast_price

st.set_page_config(page_title="CryptoWatch-AI", page_icon="🚀", layout="wide")

st.title("🪙 CryptoWatch-AI — Real-Time Crypto Insights")

coins = ["bitcoin", "ethereum", "tether", "dogecoin"]

selected_coin = st.selectbox("Select Cryptocurrency", coins)

# Current Price
price = fetch_current_price(selected_coin)

if price is not None:
    st.metric(f"{selected_coin.upper()} Price (USD)", f"${price:,.2f}")
else:
    st.error("⚠ Error fetching current price. Try again later.")

# Historical Data
history_df = fetch_historical_prices(selected_coin)

st.subheader("📈 Last 7 Days Price Trend")

if not history_df.empty:
    st.line_chart(history_df["price"])
else:
    st.warning("⚠ Historical data unavailable now. Please retry later.")

# Forecast Chart
st.subheader("🔮 Simple Price Forecast")
forecast_df = forecast_price(history_df["price"]) if not history_df.empty else None

if forecast_df is not None:
    st.line_chart(forecast_df)
else:
    st.info("Forecast will appear once history loads!")
