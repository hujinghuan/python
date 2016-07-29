# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame

df3=DataFrame({'lkey':['b','b','a','c','a','a','b'],'data1':range(7)})
df4=DataFrame({'rkey':['b','b','d'],'data2':range(3)})
pd.merge(df3,df4,left_on='lkey',right_on='rkey')