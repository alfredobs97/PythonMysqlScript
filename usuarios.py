#!/usr/bin/python
import MySQLdb
db = MySQLdb.connect(host="192.168.8.16",
                    user="root",
                    passwd="1234",
                    db="mysql")
def ver(db):
    try:
        cur = db.cursor()
        cur.execute("select User from mysql.user;")
        rows = cur.fetchall()
        for row in rows:
            print "Usuario: " + row[0]
    except:
        print "Error ejecutando esta funcion"
def add(db):
    try:
        user = raw_input("Introducir nombre del usuario: ")
        lugar = raw_input("Permisos lugar: ")
        password = raw_input("Password del usuario: ")
        cur = db.cursor()
        cur.execute("CREATE USER'" + user + "'@'" + lugar + "' IDENTIFIED BY '"+ password +"';")
        elegir = raw_input("Desea ver si se han efectuado los cambios?[s/n]")
        if elegir == 's':
            ver(db)
        else:
            print("Funcion terminada")
    except:
        print ("Error ejecutando esta funcion")
def privilegios(db):
    try:
        user = raw_input("Introducir nombre del usuario: ")
        lugar = raw_input("Permisos lugar: ")
        cur = db.cursor()
        cur.execute("SHOW GRANTS FOR '" + user + "'@'" + lugar + "';")
        rows = cur.fetchall()
        for row in rows:
            print row[0]
    except:
        print "Error ejecutando esta funcion"
eleccion = raw_input("Desea ver los usuarios(v),crear usuario(c) o ver privilegios(p)?")
if eleccion == 'v':
    ver(db)
elif eleccion == 'c':
    add(db)
elif eleccion == 'p':
    privilegios(db)
