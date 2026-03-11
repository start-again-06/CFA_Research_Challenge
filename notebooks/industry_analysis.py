# Purpose: Analyze industry growth, market trends, and macroeconomic indicators

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
industry_ticker = "XLK"  
data = yf.download(industry_ticker, period="10y")
data.head()
plt.figure(figsize=(10,5))
plt.plot(data['Close'])
plt.title("Industry Price Trend")
plt.xlabel("Date")
plt.ylabel("Price")
plt.show()
start_price = data['Close'].iloc[0]
end_price = data['Close'].iloc[-1]

years = len(data)/252

cagr = (end_price/start_price)**(1/years)-1

print("Industry CAGR:", cagr)
