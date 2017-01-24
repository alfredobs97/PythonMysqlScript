#!/usr/bin/python
import MySQLdb
db = MySQLdb.connect(host="192.168.8.16",
                    user="root",
                    passwd="1234",
                    db="mysql")
cur = db.cursor()
cur.execute("select User from mysql.user;")
rows = cur.fetchall()

for row in rows:
    print "Usuario: " + row[0]
