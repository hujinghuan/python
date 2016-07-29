import mysql.connector

cnx = mysql.connector.connect(user='hujinghuan', password='nY5jRzgBK$fZ$#ts',
                              host='115.28.2.186',
                              database='hsh_ver2')
cursor = cnx.cursor()

query = ("SELECT order_price,DATE_FORMAT(updated, '%Y-%m-%d') AS updated "
"FROM hsh_order "
"WHERE updated >= '2016-01-01' ORDER BY updated ASC")

cursor.execute(query)

for (order_price,updated) in cursor:
  print("{},{}".format(order_price,updated))

cursor.close()
cnx.close()  