import requests
import pandas as pd

url = "https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"

headers = {
"User-Agent": "Mozilla/5.0"
}

session = requests.Session()

response = session.get(url, headers=headers)

data = response.json()

records = data["records"]["data"]

call_oi = 0
put_oi = 0

for r in records:

    if "CE" in r:
        call_oi += r["CE"]["openInterest"]

    if "PE" in r:
        put_oi += r["PE"]["openInterest"]

pcr = put_oi / call_oi

print("Put Call Ratio:", pcr)
