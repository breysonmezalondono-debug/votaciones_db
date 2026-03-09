from flask import Flask, render_template, request
import mysql.connector
import config

app = Flask(__name__)

def conectar_db():
    return mysql.connector.connect(
        host=config.DB_HOST,
        user=config.DB_USER,
        password=config.DB_PASSWORD,
        database=config.DB_NAME
    )

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/registro', methods=['GET','POST'])
def registro():

    if request.method == 'POST':

        numero = request.form['numero']
        nombre = request.form['nombre']
        puesto = request.form['puesto']

        conexion = conectar_db()
        cursor = conexion.cursor()

        sql = f"""
        INSERT INTO ciudadanos(numero_identificacion,nombre,puesto_id)
        VALUES('{numero}','{nombre}','{puesto}')
        """

        cursor.execute(sql)

        conexion.commit()
        conexion.close()

        return "Ciudadano registrado"

    return render_template('registro.html')


@app.route('/consulta', methods=['GET','POST'])
def consulta():

    if request.method == 'POST':

        numero = request.form['numero']

        conexion = conectar_db()
        cursor = conexion.cursor(dictionary=True)

        sql = f"""
        SELECT c.numero_identificacion,p.lugar,p.direccion,p.mesa,p.zona
        FROM ciudadanos c
        JOIN puestos_votacion p ON c.puesto_id = p.id
        WHERE c.numero_identificacion = '{numero}'
        """

        cursor.execute(sql)

        datos = cursor.fetchone()

        conexion.close()

        return render_template('resultado.html',datos=datos)

    return render_template('consulta.html')


if __name__ == '__main__':
    app.run(debug=True)