import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
## Simple Nasdaq Price App

"""
)

tickerSymbol = 'NDX'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start='2020-01-01', end='2021-12-24')

st.write(""" ## Price of NASDAQ """)
st.line_chart(tickerDf.Volume)
st.write(""" ## Volume of NASDAQ """)
st.line_chart(tickerDf.Close)
