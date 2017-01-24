#!/usr/bin/python
import MySQLdb
db = MySQLdb.connect(host="192.168.8.16",
                    user="root",
                    passwd="1234",
                    db="mysql")
cur = db.cursor()
cur.execute("SHOW VARIABLES LIKE 'version'")
ver = cur.fetchall()
cur.execute("SHOW VARIABLES LIKE '%server_id%'")
ver2 = cur.fetchall()
cur.execute("SHOW VARIABLES LIKE 'basedir'")
ver3 = cur.fetchall()
final = [row[1] for row in ver]
print "Version de MySQL: %s"  %final
final = [row[1] for row in ver2]
print "Servidor: %s"  %final
final = [row[1] for row in ver3]
print "Directorio de las bases de datos: %s" %final
