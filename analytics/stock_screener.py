import yfinance as yf
import pandas as pd

nifty50 = [
"RELIANCE.NS","TCS.NS","INFY.NS","HDFCBANK.NS","ICICIBANK.NS"
]

results = []

for stock in nifty50:

    ticker = yf.Ticker(stock)

    info = ticker.info

    pe = info.get("trailingPE")
    roe = info.get("returnOnEquity")

    if pe and roe:

        if pe < 25 and roe > 0.15:

            results.append({
                "stock": stock,
                "pe": pe,
                "roe": roe
            })

df = pd.DataFrame(results)

print(df)
