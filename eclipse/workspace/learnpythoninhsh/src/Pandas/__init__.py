# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from scipy import  stats
import matplotlib.pyplot as plt
import pandas_datareader as pdr
import pandas_datareader.data as web
from pandas.core.frame import DataFrame
from lxml.html import parse
from urllib2 import urlopen

hsh_order=pd.read_csv('hsh_order.csv')
print(hsh_order.head(10))