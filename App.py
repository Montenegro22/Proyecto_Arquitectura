#!/usr/bin/python3
#CONTROLADOR
import mysql.connector
from mysql.connector import errorcode
import cgi
import os
from Dao import add_pelicula
from Dao import actualizar_pelicula
from Dao import eliminar_pelicula
from Dao import listar_pelicula
from modelos import Pelicula
from flask import Flask, render_template, request, redirect, url_for, flash
from flask import Flask
from flask_mysqldb import MySQL


app = Flask(__name__)


print ('Content-Type: text/json')
print ('')


datos= cgi.FieldStorage()

if os.environ['REQUEST_METHOD']=="POST":

   id=datos.getvalue('id')
   Nombre=datos.getvalue('Nombre')
   Genero=datos.getvalue('Genero')
   Año=datos.getvalue('Anio')
   Productora = datos.getvalue('Productora')
   Pais = datos.getvalue('Pais')
   Duracion = datos.getvalue('Duracion')
   Idiomas = datos.getvalue('Idiomas')
   Descripcion = datos.getvalue('Descripcion')

   if Pelicula.consultar_pelicula(id) is not None:
      print("{'mensaje':'Esa película ya existe'}")
   else:
      pelicula = Pelicula(id,Nombre,Genero,Año,Productora,Pais,Duracion,Idiomas,Descripcion)
      
      if add_pelicula(pelicula):
         print("{'mensaje':'Esa película ya existe'}")
      else:
         print("{'mensaje':'Error al crear pelicula'}")   


elif os.environ['REQUEST_METHOD']=="PUT":
#ACTUALIZAR

   id=datos.getvalue('id')
   Nombre=datos.getvalue('Nombre')
   Genero=datos.getvalue('Genero')
   Año=datos.getvalue('Anio')
   Productora = datos.getvalue('Productora')
   Pais = datos.getvalue('Pais')
   Duracion = datos.getvalue('Duracion')
   Idiomas = datos.getvalue('Idiomas')
   Descripcion = datos.getvalue('Descripcion')

   if Pelicula.actualizar_pelicula(id) is not None:
      print("{'mensaje':'Esa película ya existe'}")
   else:
      pelicula = Pelicula(id,Nombre,Genero,Año,Productora,Pais,Duracion,Idiomas,Descripcion)
      
      if actualizar_pelicula(pelicula):
         print("{'mensaje':'Esa película ya existe'}")
      else:
         print("{'mensaje':'Error al crear pelicula'}")   


elif os.environ['REQUEST_METHOD']=="DELETE":
#ELIMINAR

   id=datos.getvalue('id')
   Nombre=datos.getvalue('Nombre')
   Genero=datos.getvalue('Genero')
   Año=datos.getvalue('Anio')
   Productora = datos.getvalue('Productora')
   Pais = datos.getvalue('Pais')
   Duracion = datos.getvalue('Duracion')
   Idiomas = datos.getvalue('Idiomas')
   Descripcion = datos.getvalue('Descripcion')

   if Pelicula.eliminar_pelicula(id) is not None:
      print("{'mensaje':'Esa película ya existe'}")
   else:
      pelicula = Pelicula(id,Nombre,Genero,Año,Productora,Pais,Duracion,Idiomas,Descripcion)
      
      if eliminar_pelicula(pelicula):
         print("{'mensaje':'Esa película ya existe'}")
      else:
         print("{'mensaje':'Error al crear pelicula'}")   


elif os.environ['REQUEST_METHOD']=="GET":
#LISTAR

   id=datos.getvalue('id')
   Nombre=datos.getvalue('Nombre')
   Genero=datos.getvalue('Genero')
   Año=datos.getvalue('Anio')
   Productora = datos.getvalue('Productora')
   Pais = datos.getvalue('Pais')
   Duracion = datos.getvalue('Duracion')
   Idiomas = datos.getvalue('Idiomas')
   Descripcion = datos.getvalue('Descripcion')

   if Pelicula.listar_pelicula(id) is not None:
      print("{'mensaje':'Esa película ya existe'}")
   else:
      pelicula = Pelicula(id,Nombre,Genero,Año,Productora,Pais,Duracion,Idiomas,Descripcion)
      
      if listar_pelicula(pelicula):
         print("{'mensaje':'Esa película ya existe'}")
      else:
         print("{'mensaje':'Error al crear pelicula'}")   
















      




