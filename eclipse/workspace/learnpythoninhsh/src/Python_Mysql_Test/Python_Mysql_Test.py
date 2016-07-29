#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import mysql.connector
from locale import currency

cnx = mysql.connector.connect(user='hujinghuan', password='nY5jRzgBK$fZ$#ts',
                              host='115.28.2.186',
                              database='hsh_ver2')
cursor = cnx.cursor()

query = ("SELECT t.item_no,round(o.order_price,0),DATE_FORMAT(o.updated, '%Y-%m-%d') AS updated,o.currency "
         "FROM hsh_order o "
         "INNER JOIN hsh_trade_list t ON (t.id = o.supply_id OR t.id = o.demand_id) "
         "INNER JOIN hsh_user_title u ON (u.id = o.supply_title_id) "
         "INNER JOIN hsh_user_title ut ON (ut.id = o.demand_title_id) "
         "INNER JOIN hsh_product p ON (p.id = o.product_id) "
         "WHERE t.item_no = '7000F' AND (o.updated >= '2016-01-01') AND u.company_name <> '化塑汇测试' "
         "ORDER BY o.updated ASC ")

cursor.execute(query)

for (item_no,order_price,updated,currency) in cursor: # selection下的变量都要选取到for语句中
  print("{},{},{}".format(item_no,order_price,updated))

cursor.close()

cnx.close()  