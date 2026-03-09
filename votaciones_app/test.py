import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="votaciones_db",
    port=3306
)

print("Conectado correctamente")