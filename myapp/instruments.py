import yfinance as yf
from yfinance.utils import empty_df
import numpy as np
import pandas as pd


def getPrice(tycker):
    return yf.download(tickers=tycker, period='1d', interval='1h').iloc[-2]['Adj Close']


# metti il download direttamente qua dentro
def calculate_ema(tycker, timeframe, periods, smoothing=2):
    prices = yf.download(tickers=tycker, period='max',
                         interval=timeframe)['Adj Close']
    ema = [sum(prices[:periods]) / periods]
    for price in prices[periods:]:
        ema.append((price * (smoothing / (1 + periods))) +
                   ema[-1] * (1 - (smoothing / (1 + periods))))
    return ema[-1]


def calculate_MA(df, periods):
    return df.rolling(periods).mean()[-1]


