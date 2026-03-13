import yfinance as yf
import pandas as pd

nifty50 = [
"RELIANCE.NS","TCS.NS","INFY.NS","HDFCBANK.NS","ICICIBANK.NS",
"KOTAKBANK.NS","LT.NS","ITC.NS","SBIN.NS","BHARTIARTL.NS"
]

results = []

for stock in nifty50:

    ticker = yf.Ticker(stock)

    hist = ticker.history(period="3mo")

    hist["MA20"] = hist["Close"].rolling(20).mean()
    hist["MA50"] = hist["Close"].rolling(50).mean()

    latest = hist.iloc[-1]

    if latest["MA20"] > latest["MA50"]:
        trend = "Bullish"
    else:
        trend = "Bearish"

    results.append({
        "stock": stock,
        "trend": trend,
        "price": round(latest["Close"],2)
    })

df = pd.DataFrame(results)

print("\nMomentum Signals\n")
print(df)
