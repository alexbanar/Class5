import pymysql

# Establishing a connection to DB
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='zagadaga369', db='users')
conn.autocommit(True)

# Getting a cursor from Database
cursor = conn.cursor()

# Inserting data into table
cursor.execute("INSERT into users.users (name, id) VALUES ('john', 5)")

cursor.close()
conn.close()