# -*- coding: utf-8 -*-
"""

Created on Thur July 15 6:48:30 2022

@author: Sherry
"""

#import libs
import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import datetime

#Add a title to the dashboard
st.title('Lit Finance Dashboard')
#add tickers
tickers = ('NFLX','NVDA','AMZN','TSLA','AAPL','BTC-USD')
#add dropdown menu
dropdown = st.multiselect('Pick your assets', 
                          tickers)
#selecting dates
start = st.date_input('Start', value = pd.to_datetime('2021-01-01'))
end = st.date_input('End', value = pd.to_datetime('today'))

#relative 
def relativeret(df):
    rel = df.pct_change()
    cumret = (1+rel).cumprod() - 1
    cumret = cumret.fillna(0)
    return cumret

#define data
if len(dropdown) > 0:
    #df = yf.download(dropdown, start, end)['Adj Close']
    df = relativeret(yf.download(dropdown, start, end)['Adj Close'])
    st.header('Returns of {}'.format(dropdown))
    st.line_chart(df)
