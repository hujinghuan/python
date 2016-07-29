#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from scipy import  stats
import matplotlib.pyplot as plt
import csv

df=pd.read_csv(r'e:\Liv-ex Fine Wine Investables Series & Graph.csv')
print df.head(10)