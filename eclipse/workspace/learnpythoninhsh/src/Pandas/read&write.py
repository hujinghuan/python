# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.core.frame import DataFrame


wine=pd.DataFrame(pd.read_excel('e:\Liv-ex Fine Wine Investables Series & Graph.xls'),columns=['date','indicator'])
#wine2 = wine.set_index(['date'])
print(wine.dtypes)
print(wine[wine['date'] >='2000-03']) #dtypes=datetime64[ns],可以直接进行此操作
#print(wine2)
plt.plot(wine)
plt.show()