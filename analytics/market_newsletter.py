import yfinance as yf
import pandas as pd
import ollama
from datetime import date

nifty = yf.Ticker("^NSEI")
data = nifty.history(period="2d")

open_price = data["Open"][-1]
close_price = data["Close"][-1]
change = close_price - open_price
pct = (change/open_price)*100

stocks = [
"RELIANCE.NS","TCS.NS","INFY.NS","HDFCBANK.NS","ICICIBANK.NS"
]

summary_data = []

for s in stocks:

    ticker = yf.Ticker(s)
    hist = ticker.history(period="2d")

    change = hist["Close"][-1] - hist["Close"][-2]

    summary_data.append({
        "stock": s,
        "change": round(change,2)
    })

df = pd.DataFrame(summary_data)

top_gainers = df.sort_values("change",ascending=False).head(3)
top_losers = df.sort_values("change").head(3)

prompt = f"""
You are a financial analyst writing a daily stock market newsletter.

Nifty Open: {open_price}
Nifty Close: {close_price}
Change: {pct:.2f} %

Top Gainers:
{top_gainers}

Top Losers:
{top_losers}

Write a short professional market summary.
"""

response = ollama.chat(
    model="mistral",
    messages=[{"role":"user","content":prompt}]
)

print("\nDaily Market Newsletter\n")
print(response["message"]["content"])
