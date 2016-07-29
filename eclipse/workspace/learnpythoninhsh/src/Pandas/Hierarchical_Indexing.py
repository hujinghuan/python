# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from pandas import Series
from pandas.core.frame import DataFrame


data=Series(np.random.randn(10),index=[1,2,3,4,5,6,7,8,9,10])
print(data)