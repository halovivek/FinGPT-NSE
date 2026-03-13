import ollama
from rag.query_engine import retrieve_context

def ask_nse_ai(question):

    context = retrieve_context(question)

    prompt = f"""
You are an expert financial analyst focused on Nifty 50 stocks.

Context:
{context}

Question:
{question}

Give a clear financial explanation.
"""

    response = ollama.chat(
        model="mistral",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]
