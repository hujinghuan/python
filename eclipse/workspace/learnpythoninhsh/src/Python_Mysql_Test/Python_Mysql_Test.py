#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
import matplotlib.pyplot as plt
sys.setdefaultencoding('utf-8')
import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame
import xlwt

import datetime
import mysql.connector
from locale import currency

cnx = mysql.connector.connect(user='hujinghuan', password='nY5jRzgBK$fZ$#ts',
                              host='115.28.2.186',
                              database='hsh_ver2')
cursor = cnx.cursor()

query = ("SELECT round(IF(hsh_order.order_price>2000,hsh_order.order_price,hsh_order.order_price * 1.065*1.17*6.6+150),2) AS order_price1,DATE_FORMAT(hsh_order.updated, '%Y-%m-%d') AS updated,hsh_product.item_no "
         "FROM hsh_order "
         "INNER JOIN hsh_product ON (hsh_product.id = hsh_order.product_id) "
         "ORDER BY hsh_order.updated ASC ")

cursor.execute(query)

#fp = open('e:/123.csv','wb'),写入文件
for (order_price1,updated,item_no) in cursor: # selection下的变量都要选取到for语句中
    data=("{},{},{}".format(order_price1,updated,item_no))
    print(data)
    #fp.write(data)
    #fp.close

cursor.close()

cnx.close()  
