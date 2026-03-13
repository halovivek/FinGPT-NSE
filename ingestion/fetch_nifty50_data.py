import yfinance as yf
import pandas as pd
import json

nifty50 = [
"RELIANCE.NS","TCS.NS","INFY.NS","HDFCBANK.NS","ICICIBANK.NS",
"KOTAKBANK.NS","LT.NS","HINDUNILVR.NS","ITC.NS","SBIN.NS",
"BHARTIARTL.NS","ASIANPAINT.NS","AXISBANK.NS","MARUTI.NS",
"BAJFINANCE.NS","BAJAJFINSV.NS","TITAN.NS","SUNPHARMA.NS",
"WIPRO.NS","ULTRACEMCO.NS","NESTLEIND.NS","NTPC.NS",
"POWERGRID.NS","ONGC.NS","COALINDIA.NS","TECHM.NS",
"HCLTECH.NS","TATASTEEL.NS","JSWSTEEL.NS","GRASIM.NS",
"INDUSINDBK.NS","ADANIENT.NS","ADANIPORTS.NS","APOLLOHOSP.NS",
"BRITANNIA.NS","CIPLA.NS","DIVISLAB.NS","DRREDDY.NS",
"EICHERMOT.NS","HEROMOTOCO.NS","HDFCLIFE.NS","SBILIFE.NS",
"BAJAJ-AUTO.NS","TATACONSUM.NS","TATAMOTORS.NS","UPL.NS",
"LTIM.NS","BPCL.NS","SHREECEM.NS","HINDALCO.NS"
]

data = []

for ticker in nifty50:

    stock = yf.Ticker(ticker)

    info = stock.info

    data.append({
        "ticker": ticker,
        "name": info.get("longName"),
        "sector": info.get("sector"),
        "market_cap": info.get("marketCap"),
        "pe_ratio": info.get("trailingPE"),
        "price": info.get("currentPrice")
    })

df = pd.DataFrame(data)

df.to_json("../data/nifty50_fundamentals.json", orient="records")

print("Nifty 50 data saved")
