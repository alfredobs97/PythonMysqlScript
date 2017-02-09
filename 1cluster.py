from cassandra.cluster import Cluster
import os
import sys
print ("Bienvenido al script de administracion de Cassandra")
ip  = raw_input("Seleccione la ip de su servidor: ")
puerto = raw_input("Seleccione el puerto de su servidor (por defecto 9042): ")
cluster = Cluster(contact_points=[ip],port=puerto)
session = cluster.connect()
if session:
    equipo = raw_input("Desea ver sobre que servidor trabaja?(s/n)")
    if equipo =='s':
        host = os.system("cqlsh " + ip + " " + puerto + " --cqlversion=3.4.4 -e 'SHOW HOST'")
        print host
    else:
        print ""
    db = raw_input("Quiere ver las keyspaces disponibles?(s/n)")
    if db == 's':
        verdb = os.system("cqlsh " + ip + " " + puerto + " --cqlversion=3.4.4 -e 'DESCRIBE KEYSPACES;'")
        print verdb
    else:
        print ""
    seleccionarKeyspace = raw_input("Seleccionar la keyspace con la que se va a trabajar: ")
    session.set_keyspace(seleccionarKeyspace)
    verdatos = raw_input("Desea ver los datos?")
    if verdatos == 's':
        tabla = raw_input("Seleccione el nombre de la tabla")
        datos = session.execute("SELECT * FROM " + tabla + ";")
        print datos[0]
else:
    print ("Error al conectar a Cassandra")
