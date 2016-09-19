#!/usr/bin/python  
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from scipy import  stats
import matplotlib.pyplot as plt
import pandas_datareader as pdr
from pandas.core.frame import DataFrame
from datetime import datetime


hsh_order=pd.read_excel('hsh_order.xls',header=None)

hsh_order.columns = ['item_no', 'product_no','order_price','order_quantity','total_price','order_date','currency','order_place','supply_company','demand_comapny']
print(hsh_order.columns)

hsh_order['order_date'] = pd.to_datetime(hsh_order['order_date'])

print(hsh_order.head())
print(hsh_order.dtypes)
#print(hsh_order[hsh_order['order_date'] >='20140105'].head(50))
print(hsh_order[(hsh_order['item_no']=='7000F') & (hsh_order['order_date'] >='20160201')].sort_values(by=['total_price'],ascending=[1])).head() #这里要打==，两个=号,ascending=[1]表示升序，[0]表示降序
