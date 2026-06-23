# Multi-Asset Brazilian Stock Market Analysis (5 Assets)

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# 1. Define assets
# -----------------------------
tickers = ['EGIE3.SA','ITSA4.SA','BBAS3.SA','PSSA3.SA','^BVSP']

# -----------------------------
# 2. Download data
# -----------------------------
data = yf.download(tickers, period='10y')['Close']

# -----------------------------
# 3. Monthly returns
# -----------------------------
monthly = data.resample("M").last().pct_change() * 100

# IBOV analysis
ibov_monthly = monthly['^BVSP']

ibov_monthly.groupby(monthly.index.month).mean().plot.bar(
    figsize=(12,5),
    title="IBOV Monthly Average Returns"
)

plt.grid()
plt.show()

# -----------------------------
# 4. Annual returns
# -----------------------------
annual = data.resample("Y").last().pct_change() * 100

summary = pd.DataFrame({
    "Positive Years": (annual > 0).sum(),
    "Negative Years": (annual < 0).sum(),
    "% Positive": (annual > 0).mean() * 100
})

print(summary)

# -----------------------------
# 5. Moving averages function (reusable)
# -----------------------------
def plot_moving_average(df, ticker):
    ma20 = df[ticker].rolling(20).mean()
    ma200 = df[ticker].rolling(200).mean()

    plt.figure(figsize=(12,5))
    plt.plot(df[ticker], label=ticker, alpha=0.5)
    plt.plot(ma20, label='MA20')
    plt.plot(ma200, label='MA200')

    plt.title(f"Moving Average Strategy - {ticker}")
    plt.legend()
    plt.grid()
    plt.show()

# -----------------------------
# 6. Apply to all stocks
# -----------------------------
for t in ['EGIE3.SA','ITSA4.SA','BBAS3.SA','PSSA3.SA']:
    plot_moving_average(data, t)
