#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from scipy import  stats
import matplotlib.pyplot as plt
import statsmodels.api as sm
from pandas.core.frame import DataFrame
import pandas_datareader.data as web

names=['AAPL','GOOG','MSFT','DELL','GS','MS','BAC','C']
def get_px(stock,start,end):
    return web.get_data_yahoo(stock,start,end)['Adj Close']
px=DataFrame({n:get_px(n,'1/1/2009','6/1/2012') for n in names})

px=px.asfreq('B').fillna(method='pad')
rets=px.pct_change()
((1+rets).cumprod()-1).plot()
plt.show()