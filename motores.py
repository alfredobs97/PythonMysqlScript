#!/usr/bin/python
import MySQLdb
db = MySQLdb.connect(host="192.168.8.16",
                    user="root",
                    passwd="1234",
                    db="mysql")
cur = db.cursor()
cur.execute("SHOW ENGINES")
ver = cur.fetchall()
print "Version de Mysql : %s" %ver
