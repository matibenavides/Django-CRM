import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '321654987'
)

cursorObject = dataBase.cursor()

# Mostrar todas las bases de datos
cursorObject.execute("SHOW DATABASES")

print("Bases de datos existentes:")
for db in cursorObject:
    print(db[0])

dataBase.close()
