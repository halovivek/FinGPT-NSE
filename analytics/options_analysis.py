from ingestion.fetch_options_chain import pcr

def analyze_market():

    if pcr > 1.2:
        return "Bullish sentiment"

    elif pcr < 0.7:
        return "Bearish sentiment"

    else:
        return "Neutral market sentiment"

print(analyze_market())
