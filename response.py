#!/usr/bin/python3
import mysql.connector
from mysql.connector import errorcode
import cgi

print('Content-Type: text/html')
print('')

datos= cgi.FieldStorage()
nombre=datos.getvalue('nombre')
contraseña =datos.getvalue('contra')

try:
  cnx = mysql.connector.connect(user='Pelicula', password = 'Nat.2008', database='Peliculas', host='127.0.0.1')
  cursor = cnx.cursor()
  sql = "insert into Correo (Usuario,Contraseña) values (%s,sha(%s));"
  cursor.execute(sql,(nombre,contraseña))
  cursor.close()
  cnx.commit()
  print('<p>Usuario creado {}</p>'.format(nombre))
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Algo está mal con tu usuario o contraseña")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Base de Datos no existe")
  else:
    print(err)
else:
    cnx.close()
