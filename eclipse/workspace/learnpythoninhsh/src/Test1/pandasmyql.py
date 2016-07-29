# -*- coding: utf-8 -*-
import pandas as pd
import MySQLdb

conn = MySQLdb.connect(host="115.28.2.186",user="hujinghuan",passwd="nY5jRzgBK$fZ$#ts",db="hsh_ver2")

# read
sql = ("SELECT o.id,t.item_no,round(o.order_price,0),DATE_FORMAT(o.updated, '%Y-%m-%d') AS updated,o.currency "
         "FROM hsh_order o "
         "INNER JOIN hsh_trade_list t ON (t.id = o.supply_id OR t.id = o.demand_id) "
         "INNER JOIN hsh_user_title u ON (u.id = o.supply_title_id) "
         "INNER JOIN hsh_user_title ut ON (ut.id = o.demand_title_id) "
         "INNER JOIN hsh_product p ON (p.id = o.product_id) "
         "WHERE o.order_price BETWEEN 7000 and 150000 AND o.currency = 1 AND t.item_no = '7000F' AND (o.updated >= '2016-01-01') AND u.company_name <> '化塑汇测试' "
         "ORDER BY o.updated ASC ")
df = pd.read_sql(sql,conn,index_col='item_no' )
print df
