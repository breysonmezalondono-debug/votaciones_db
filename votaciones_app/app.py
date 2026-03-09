from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Conexión a la base de datos
def conectar_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="#Sd512177926",
        database="votaciones_db",
        port=3306
    )
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        numero = request.form['numero']
        nombre = request.form['nombre']
        puesto_id = request.form['puesto']

        conexion = conectar_db()
        cursor = conexion.cursor()

        sql = "INSERT INTO ciudadanos (identificacion, nombre, puesto_id) VALUES (%s, %s, %s)"
        valores = (numero, nombre, puesto_id)
        cursor.execute(sql, valores)

        conexion.commit()
        conexion.close()

        return "Ciudadano registrado correctamente"

    return render_template('registro.html')

@app.route('/consulta', methods=['GET', 'POST'])
def consulta():
    if request.method == 'POST':
        numero = request.form['numero']

        conexion = conectar_db()
        cursor = conexion.cursor(dictionary=True)

        sql = f"""
       SELECT c.identificacion, p.lugar, p.direccion, p.mesa, p.zona
FROM ciudadanos c
JOIN puestos_votacion p ON c.puesto_id = p.id
WHERE c.identificacion = %s
        """

        cursor.execute(sql, (numero,))
        resultado = cursor.fetchone()
        conexion.close()

        return render_template('resultado.html', datos=resultado)

    return render_template('consulta.html')

if __name__ == '__main__':
    app.run(debug=True)