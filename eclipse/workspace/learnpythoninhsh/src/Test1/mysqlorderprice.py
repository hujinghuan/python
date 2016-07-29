# -*- coding: utf-8 -*-
import pandas as pd
import MySQLdb
import numpy as np
import pylab as pl
import matplotlib.dates as dt
from numpy import dtype


conn = MySQLdb.connect(host="115.28.2.186",user="hujinghuan",passwd="nY5jRzgBK$fZ$#ts",db="hsh_ver2")

# read
sql_y = ("SELECT round(o.order_price,0) "
         "FROM hsh_order o "
         "INNER JOIN hsh_trade_list t ON (t.id = o.supply_id OR t.id = o.demand_id) "
         "INNER JOIN hsh_user_title u ON (u.id = o.supply_title_id) "
         "INNER JOIN hsh_user_title ut ON (ut.id = o.demand_title_id) "
         "INNER JOIN hsh_product p ON (p.id = o.product_id) "
         "WHERE o.order_price BETWEEN 7000 and 150000 AND o.currency = 1 AND t.item_no = '7000F' AND (o.updated >= '2016-01-01') AND u.company_name <> '化塑汇测试' "
         "ORDER BY o.updated ASC ")
y = pd.read_sql(sql_y,conn)


sql_x = ("SELECT o.updated "
         "FROM hsh_order o "
         "INNER JOIN hsh_trade_list t ON (t.id = o.supply_id OR t.id = o.demand_id) "
         "INNER JOIN hsh_user_title u ON (u.id = o.supply_title_id) "
         "INNER JOIN hsh_user_title ut ON (ut.id = o.demand_title_id) "
         "INNER JOIN hsh_product p ON (p.id = o.product_id) "
         "WHERE o.order_price BETWEEN 7000 and 150000 AND o.currency = 1 AND t.item_no = '7000F' AND (o.updated >= '2016-01-01') AND u.company_name <> '化塑汇测试' "
         "ORDER BY o.updated ASC ")

x = np.read_sql(sql_x,conn,dtype='datetime64[ns]')
pl.plot(x,y,label="$7000F$",color="red",linewidth=2)
pl.show()
