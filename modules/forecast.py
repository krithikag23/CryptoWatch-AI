import pandas as pd

def forecast_price(series):
    # Return None if insufficient data
    if len(series) == 0:
        return None
    
    last_price = series.iloc[-1]
    forecast_values = [last_price * (1 + 0.01*i) for i in range(1, 6)]
    future_index = pd.date_range(start=series.index[-1], periods=5, freq='D')
    df = pd.DataFrame(forecast_values, index=future_index, columns=["Forecast"])
    return df
