import matplotlib.pyplot as plt

def plot_price_chart(df):
    plt.figure(figsize=(8, 4))
    plt.plot(df.index, df["price"])
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.title("Crypto Price Trend")
    plt.tight_layout()
    return plt
