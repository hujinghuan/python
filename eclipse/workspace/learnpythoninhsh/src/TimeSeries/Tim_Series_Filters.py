#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

dta = sm.datasets.macrodata.load_pandas().data

index = pd.Index(sm.tsa.datetools.dates_from_range('1959Q1', '2009Q3')) #选择1959q1-2009q3的数据
print(index)
dta.index = index
del dta['year']
del dta['quarter']
print(sm.datasets.macrodata.NOTE)
print(dta.head(10))

fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111)
dta.realgdp.plot(ax=ax);
legend = ax.legend(loc = 'upper left');
legend.prop.set_size(20);
plt.show()

gdp_cycle, gdp_trend = sm.tsa.filters.hpfilter(dta.realgdp)

gdp_decomp = dta[['realgdp']]
gdp_decomp["cycle"] = gdp_cycle
gdp_decomp["trend"] = gdp_trend

fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111)
gdp_decomp[["realgdp", "trend"]]["2000-03-31":].plot(ax=ax, fontsize=16);
legend = ax.get_legend()
legend.prop.set_size(20);
plt.show()

bk_cycles = sm.tsa.filters.bkfilter(dta[["infl","unemp"]])
fig = plt.figure(figsize=(12,10))
ax = fig.add_subplot(111)
bk_cycles.plot(ax=ax, style=['r--', 'b-']);
plt.show()