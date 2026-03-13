import streamlit as st
from analytics.market_summary import generate_summary
from analytics.stock_screener import screen_stocks
from llm.llm_engine import ask_nse_ai

st.title("FinGPT NSE Assistant")

st.header("Daily Market Summary")

st.write(generate_summary())

st.header("AI Stock Screener")

st.write(screen_stocks())

question = st.text_input("Ask about Nifty stocks")

if question:

    answer = ask_nse_ai(question)

    st.write(answer)
