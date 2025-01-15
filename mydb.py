# Instalar Mysql en la computadora
# https.//dev.mysql.com/downloads/installer/
# pip install mysql
# pip install mysql-connector
#pip install mysql-connector-python

import mysql.connector

#Creamos la conexion a la base de datos
dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '321654987',
    auth_plugin='mysql_native_password'
)

#Preparamos un objeto cursor para las consultas

cursorObject = dataBase.cursor()

# Creamos la base de datos

cursorObject.execute("CREATE DATABASE webcrm")

# Imprimimos un mensaje para confirmar, es opcional

print("Todo listo!")