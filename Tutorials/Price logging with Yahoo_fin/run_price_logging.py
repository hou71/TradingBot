"""
1. Retrieve retrieve daily price data for a stock
2. Calculate indicators for stock (Simple moving average, bollinger band)
3. Plot stock price and indicator on chart
"""

import indicators as ind
import yahoo_fin.stock_info as stock_info
from matplotlib import pyplot as plt
import datetime as dt

def plot_stock(ax, price, stock_name=''):
    ax.plot(price, label= "{} Stock Price".format(stock_name), color="red")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.grid()
    ax.legend()
    ax.set_title("Opening Price for {} stock".format(stock_name))

if __name__ == "__main__":
    # Setup figure
    stock_name = "msft"
    fig,(ax1,ax2,ax3) = plt.subplots(nrows=3, ncols=1, figsize=(10,16))

    # Get stock price data
    price_data = stock_info.get_data(stock_name, start_date="01/01/2020", end_date="01/01/2022")['open']
    # Calculate
    sma, sma_action= ind.calculate_sma(price_data, period=7)
    (BBP, price_BB, upper_BB, lower_BB), bb_action = ind.calculate_bb(price_data)

    #Plot stock price and indicators
    plot_stock(ax1, price_data, stock_name)
    ind.plot_sma(ax2,price_data, sma)
    ind.plot_BB(ax3, price_BB, upper_BB, lower_BB)

    plt.savefig("Stock Price and indicators.png")




