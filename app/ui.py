import streamlit as st
from analytics.market_newsletter import *
from analytics.momentum_engine import *
from analytics.portfolio_ai import *

st.title("FinGPT NSE AI Platform")

st.header("Daily Market Newsletter")
st.write(generate_newsletter())

st.header("Momentum Signals")
st.write(run_momentum_engine())

st.header("AI Portfolio Suggestion")
st.write(generate_portfolio())

question = st.text_input("Ask about Nifty stocks")
