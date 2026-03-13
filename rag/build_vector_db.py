import json
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

with open("../data/nifty50_fundamentals.json") as f:
    stocks = json.load(f)

docs = []

for s in stocks:

    text = f"""
    Company: {s['name']}
    Ticker: {s['ticker']}
    Sector: {s['sector']}
    Market Cap: {s['market_cap']}
    PE Ratio: {s['pe_ratio']}
    Price: {s['price']}
    """

    docs.append(text)

db = Chroma.from_texts(
    docs,
    embedding,
    persist_directory="../data/vector_db"
)

db.persist()

print("Vector DB created")
