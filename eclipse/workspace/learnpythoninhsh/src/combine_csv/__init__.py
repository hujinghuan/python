#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from scipy import  stats
import matplotlib.pyplot as plt
import csv

BI_3731=pd.read_csv(r'C:\Users\Administrator\Desktop\BI\3731.csv')
print BI_3731.head(10)
BI_3731 = BI_3731.sort_values(by="销售金额",ascending=[1])

BI_0509=pd.read_csv(r'C:\Users\Administrator\Desktop\BI\0509.csv')
# print BI_0509.head(10)

# print(BI_3731["销售金额"].sum(), BI_3731["销售金额"].mean(),BI_3731["销售金额"].min(),BI_3731["销售金额"].max())