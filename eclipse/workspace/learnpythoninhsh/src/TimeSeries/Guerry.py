#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import statsmodels.api as sm
from patsy import dmatrices
import matplotlib.pyplot as plt

url='http://vincentarelbundock.github.com/Rdatasets/csv/HistData/Guerry.csv'
df=pd.read_csv(url)

print df.head() #前5条记录

vars=['Department','Lottery','Literacy','Wealth','Region'] #筛选需要的字段
df=df[vars]
print df.tail() #后5条记录
df=df.dropna()
y,X=dmatrices('Lottery~Literacy+Wealth+Region',data=df,return_type='dataframe')
print y.head()
print X.head()

mod=sm.OLS(y,X)
res=mod.fit()
print res.summary()

print sm.stats.linear_rainbow(res)
sm.graphics.plot_partregress('Lottery','Wealth',['Region','Literacy'],data=df,obs_labels=False)
plt.show()
