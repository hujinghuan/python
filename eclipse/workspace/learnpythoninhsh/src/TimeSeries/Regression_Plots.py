# -*- coding: utf-8 -*-

from __future__ import print_function
from statsmodels.compat import lzip
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import ols
from enthought.units import pressure
import scimath

prestige = sm.datasets.get_rdataset("Duncan", "car", cache=True).data
print(prestige)
prestige_model = ols("prestige ~ income + education", data=prestige).fit()
print(prestige_model.summary())

fig, ax = plt.subplots(figsize=(12,8))
fig = sm.graphics.influence_plot(prestige_model, ax=ax, criterion="cooks")
plt.show()

fig, ax = plt.subplots(figsize=(12,8))
fig = sm.graphics.plot_partregress("prestige", "income", ["income", "education"], data=prestige, ax=ax)
plt.show()
