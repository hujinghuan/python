# -*- coding: utf-8 -*-

import tushare as ts
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from pandas.core.frame import DataFrame
from pandas.core.series import Series


a=DataFrame(ts.get_hist_data('000001'))
b=DataFrame(ts.get_hist_data('000002'))
c=DataFrame(ts.get_hist_data('000010'))
#print(a)
r=a.close.corr(c.close)
print(r)

"""
zxb.index = pd.to_datetime(zxb.index)
#zxb=pd.Series(zxb)
#print(zxb)

cyb=DataFrame(ts.get_hist_data('cyb'))
cyb.index = pd.to_datetime(cyb.index)
#zxb=pd.Series(zxb)
print(cyb)

r=zxb.close.corr(cyb.close)
print(r)
"""

"""
plt.xlabel('date')
plt.ylabel('close_price')
plt.plot(zxb.close,color='red')
plt.legend()
plt.show()

#zxb.to_csv('c:/000875.csv')#选择保存
"""