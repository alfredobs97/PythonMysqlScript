import pymongo
from pymongo import MongoClient
####funciones####
def insertar():
    try:
        nombre = raw_input("Nombre del alumno: ")
        edad = raw_input("Edad del alumno: ")
        hobby = raw_input("Hobby del alumno: ")
        db.tbalumnos.insert_one(
            {
            "nombre": nombre,
            "edad": edad,
            "hobby": hobby
            })
        print ("Datos introducidos correctamente")
    except Exception, e:
        print str(e)
def leer():
    try:
        col = db.tbalumnos.find()
        print '\n Listado de todos los alumnos \n'
        for coleccion in col:
            print coleccion
    except Exception, e:
        print str(e)
####fin de funciones####
conn = MongoClient('192.168.8.16',27017)
db = conn.dbalumnos
print (db)
seleccionar = raw_input("Elegir 1 para introducir datos, 2 para ver los datos: ")
if seleccionar == '1':
    insertar()
elif seleccionar == '2':
    leer()
else:
    print 'Seleccion invalida'
