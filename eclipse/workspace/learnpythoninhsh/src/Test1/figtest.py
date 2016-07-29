#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import pylab as pl
import matplotlib.dates as dt
from numpy import dtype

x=np.loadtxt(r'd:\7000F-X.csv',delimiter=',',dtype='datetime64[ns]' )
y=np.loadtxt(r'd:\7000F-Y.csv',delimiter=',',dtype='str' )

pl.plot(x,y,label="$7000F$",color="red",linewidth=2)
pl.xlabel('time')
pl.ylabel('price')
#pl.xlim(0.0,2016-07-06)
pl.ylim(8000,10000)
pl.title("2016 7000F order price")
pl.legend() #显示数据标示
#pl.show()
pl.savefig(r'd:\7000F.jpg')