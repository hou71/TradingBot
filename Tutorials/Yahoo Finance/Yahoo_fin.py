import yahoo_fin.stock_info as stock_info
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt # https://docs.python.org/3/library/datetime.html
import numpy as np

#https://theautomatic.net/yahoo_fin-documentation/#installation

def get_data(stock='aapl', startDate="1/1/2019", endDate="3/27/2023"):
    data = stock_info.get_data(ticker=stock, start_date=startDate, end_date=endDate, interval="1d")
    print(data)
    return data

def CalculateMomentum(df, period):
    rawData = df['open'].pct_change(period)

    # Calculate for the indicator action (buy, sell, hold)
    '''indicator algo: Set buy and sell momentum limit, when momentum crosses that line buy or sell, else hold'''
    resultVec = pd.DataFrame(index=df.index)
    buyThreshold = 0.1
    sellThreshold = -0.1
    momentum = np.where(np.isnan(rawData.values), 0, rawData.values)  # Replace Nan vals with 0
    action = np.where(momentum > buyThreshold, 1, 0)  # BUY
    action = np.where(momentum < sellThreshold, -1, action)  # SELL
    resultVec["Action"] = action.flatten()
    return rawData, resultVec

def plot_data(data):
    pass

if __name__ == "__main__":
    data = get_data('spy')
    momentum, actionMomentum=CalculateMomentum(data,period=14)