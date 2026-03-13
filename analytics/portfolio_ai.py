import yfinance as yf
import pandas as pd
import ollama

stocks = [
"RELIANCE.NS","TCS.NS","INFY.NS","HDFCBANK.NS","ICICIBANK.NS"
]

data = []

for s in stocks:

    ticker = yf.Ticker(s)
    info = ticker.info

    pe = info.get("trailingPE")
    roe = info.get("returnOnEquity")
    cap = info.get("marketCap")

    data.append({
        "stock": s,
        "pe": pe,
        "roe": roe,
        "market_cap": cap
    })

df = pd.DataFrame(data)

prompt = f"""
You are an equity research analyst.

Based on the following data, suggest a simple diversified portfolio
for long-term investors.

{df}

Explain the reasoning briefly.
"""

response = ollama.chat(
    model="mistral",
    messages=[{"role":"user","content":prompt}]
)

print("\nAI Portfolio Recommendation\n")
print(response["message"]["content"])
