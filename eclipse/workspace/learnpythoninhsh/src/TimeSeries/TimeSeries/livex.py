#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import pandas as pd
import numpy as np
from scipy import  stats
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.graphics.api import qqplot

"""
dta=[10930,10318,10595,10972,7706,6756,9092,10551,9722,10913,11151,8186,10930,10318,10595,10972,7706,6756,9092,10551,9722,10913,11151,8186]

dta=pd.Series(dta)
dta.index = pd.Index(sm.tsa.datetools.dates_from_range('2013m1',length=24))
dta.plot(figsize=(12,8))
plt.show()
"""

livex=np.loadtxt('e:\Liv-ex Fine Wine.csv')
livex=pd.Series(livex)
livex.index = pd.Index(sm.tsa.datetools.dates_from_range('1988m1',length=311))
#print(livex)
#plt.axis([0,311,0,400])
#livex.plot(figsize=(311,8))
#plt.show()

fig = plt.figure(figsize=(12,8))
ax1= fig.add_subplot(111)
diff1 = livex.diff(1)
diff1.plot(ax=ax1)
#plt.show()

fig = plt.figure(figsize=(12,8))
ax1 = fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(livex.values.squeeze(), lags=40, ax=ax1)
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(livex, lags=40, ax=ax2)
plt.show()

#arma_mod10 = sm.tsa.ARMA(livex, (1,0)).fit()
#print(arma_mod10.aic, arma_mod10.bic, arma_mod10.hqic)
arma_mod20 = sm.tsa.ARMA(livex, (2,0)).fit() #拟合效果最好
print(arma_mod20.aic, arma_mod20.bic, arma_mod20.hqic)
#arma_mod30 = sm.tsa.ARMA(livex, (3,0)).fit()
#print(arma_mod30.aic, arma_mod30.bic, arma_mod30.hqic)
#arma_mod11 = sm.tsa.ARMA(livex, (1,1)).fit()
#print(arma_mod11.aic, arma_mod11.bic, arma_mod11.hqic)
#arma_mod12 = sm.tsa.ARMA(livex, (1,2)).fit()
#print(arma_mod12.aic, arma_mod12.bic, arma_mod12.hqic)

resid = arma_mod20.resid
print(resid)

fig = plt.figure(figsize=(12,8))
ax1 = fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(resid.values.squeeze(), lags=24, ax=ax1)
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(resid, lags=24, ax=ax2)
#plt.show()

print(sm.stats.durbin_watson(resid.values)) #1.20386506641,不太理想

fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111)
ax = resid.plot(ax=ax);
#plt.show()

print(stats.normaltest(resid))
fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111)
fig = qqplot(resid, line='q', ax=ax, fit=True)
#plt.show()

r,q,p = sm.tsa.acf(resid.values.squeeze(), qstat=True)
data = np.c_[range(1,41), r[1:], q, p]
table = pd.DataFrame(data, columns=['lag', "AC", "Q", "Prob(>Q)"])
print(table.set_index('lag'))

predict_livex = arma_mod20.predict('2013m11', '2014m6', dynamic=True)
print(predict_livex)

fig, ax = plt.subplots(figsize=(12, 8))
ax = livex.ix['2000m1':].plot(ax=ax)
fig = arma_mod20.plot_predict('2013m11','2014m6', dynamic=True, ax=ax, plot_insample=False)
plt.show()