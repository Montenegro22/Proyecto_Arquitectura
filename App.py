#!/usr/bin/python3
import mysql.connector
from mysql.connector import errorcode
import cgi

print ('Content-Type: text/html')
print ('')

datos= cgi.FieldStorage()
Nombre=datos.getvalue('Nombre')
contrase=datos.getvalue('password')


print ("")
print ("conectando")
print ("")



try:
   conn = mysql.connector.connect(user='Pelicula', password='Nat.2008', database='Peliculas', host='127.0.0.1')
   cursor = conn.cursor()
   sql = "insert into datos(Nombre,password) values (%s,sha(%s));"
   #sql = "SELECT * FROM datos WHERE Nombre='Nombre' and contrase='password'";
   val = (Nombre, contrase)
   cursor.execute(sql,val)

   conn.commit()

   print ('<p>El usuario ya  ha sido registrado Bienvenido  {} </p>'.format(Nombre))
   cursor.close()
   conn.close()


except mysql.connector.Error as err:

   if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print ("Por favor verifique el nombre de usuario o contraseña")
   elif err.errno == errorcode.ER_BAD_BD_ERROR:
      print ("La base de datos a la que desea acceder no existe, por favor verificar conexion")
   else:
      print (err)



