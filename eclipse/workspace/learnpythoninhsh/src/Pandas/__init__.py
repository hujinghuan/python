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

parsed=parse(urlopen('http://finance.yahoo.com/q/op?s=AAPL+Options'))
doc=parsed.getroot()
print(doc)

links=doc.findall('.//a')
links[15:20]

lnk=links[28]
print(lnk.get('href'))
print(lnk.text_content())

urls=[lnk.get('href') for lnk in doc.findall('.//a')]
print(urls[-10:])