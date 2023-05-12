import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
'''
Calculae simple moving average
https://www.investopedia.com/terms/s/sma.asp
Input:
    price_data: dataframe with all the price data
    period: The window size of all the 
'''


def calculate_sma(price_data: pd.DataFrame, period=7) -> pd.DataFrame:
    sma = price_data.rolling(window=period, min_periods=period).mean()

    # Calculate for the indicator action (buy, sell, hold)
    # https://www.fidelity.com/learning-center/trading-investing/technical-analysis/technical-indicator-guide/sma

    actionVec = pd.DataFrame(index=price_data.index)
    buffer = 0
    action = np.where(price_data > sma + buffer, 1, 0)
    action = np.where(price_data < sma - buffer, -1, action)
    actionVec["Action"] = action
    return sma, actionVec


def calculate_bb(price_data: pd.DataFrame, period=7):
    # Calculate SMA
    sma,_ = calculate_sma(price_data, period)
    # Calculate STD
    std = price_data.rolling(window=period, min_periods=period).std()

    # Calculate BollingerBands
    upper_bound = sma + (2 * std)
    lower_bound = sma - (2 * std)

    bbData = ((sma - upper_bound) / (upper_bound - lower_bound),sma, upper_bound, lower_bound) # (BB%, price, upper BB, lower BB)

    # Calculate for the indicator action (buy, sell, hold)
    # https://www.investopedia.com/trading/using-bollinger-bands-to-gauge-trends/
    sma_5_day = calculate_sma(price_data, period=5)
    actionVec = pd.DataFrame(index=price_data.index)
    # action = np.where(sma_5_day[0] < oneStdDown.values, -1, 0)
    # action = np.where(sma_5_day[0] > oneStdUp.values, 1, action)
    # actionVec["Action"] = action
    return bbData, actionVec

def plot_sma(ax, price, sma):
    ax.plot(sma,label="sma", color='midnightblue', linewidth=1)
    ax.plot(price, label="price", color='red', linewidth=1)
    ax.grid()
    ax.tick_params(axis='x')
    ax.set_ylabel("Price")
    ax.set_xlabel("Date")
    ax.set_title("Simple Moving Average Indicator")
    ax.legend()


def plot_BB(ax, price, upper_BB, lower_BB):
    ax.plot(price, label="SMA", color='midnightblue', linewidth=1)
    ax.plot(upper_BB, label="BB +2\u03C3", color='seagreen', linewidth=1)
    ax.plot(lower_BB, label="BB -2\u03C3", color='seagreen', linewidth=1)
    ax.set_xlabel("Date")
    ax.set_ylabel("Normalized Price")
    ax.set_title("Bollinger Bands Indicator")
    ax.grid()
    ax.legend()