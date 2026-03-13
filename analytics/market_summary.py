import yfinance as yf
import pandas as pd
import ollama

nifty = yf.Ticker("^NSEI")

data = nifty.history(period="1d")

open_price = data["Open"][0]
close_price = data["Close"][0]

change = close_price - open_price

prompt = f"""
You are a financial analyst.

Nifty opened at {open_price} and closed at {close_price}.
Change: {change}

Write a short market summary.
"""

response = ollama.chat(
    model="mistral",
    messages=[{"role":"user","content":prompt}]
)

print(response["message"]["content"])
