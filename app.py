from flask import Flask, render_template,request
from plantapi import identificar_planta as api
from consulta_img import obtener_imagen as buscar_img
from conexion_base import inicializar_base as comprobar
from werkzeug.utils import secure_filename
import psycopg2
import uuid
import os

app = Flask(__name__)

app.config['MAX_CONTENT_LENGTH'] = 20 * 1024 * 1024  # 20 MB
    
comprobar()

# conexión a PostgreSQL
try:
    conexion = psycopg2.connect(
        host="localhost",
        database="plantas_db",
        user="postgres",
        password="plantas_db1234567890_*",
        port="5432"
    )

    print("Conexión exitosa")

except Exception as e:
    print("Error de conexión:", e)

cursor = conexion.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/upload", methods=["POST"])
def upload():
    
    UPLOAD_FOLDER = "static/uploads/"#Folder de subida
    
    archivo = request.files["imagen"]#obtener imagen del campo del formulario "imagen"
    organ=request.form["organ"]#obtener 
    
    #obtener extensiòn del archivo, para el cambio de nombre
    _, extension = os.path.splitext(secure_filename(archivo.filename))

    nuevo_nombre = str(uuid.uuid4())+extension  # nombre nuevo - no repetido

    ruta_imagen = os.path.join(
        UPLOAD_FOLDER,
        nuevo_nombre
    )
    archivo.save(ruta_imagen)

    consulta=api(UPLOAD_FOLDER,nuevo_nombre,organ,"all")

    if(consulta["nombre"]!="Indeterminado"):#subir info de la planta en caso de que no exista en db
        print("consulta",consulta["nombre"])
        cursor.execute("SELECT * FROM plantas WHERE nombre_cientifico = %s;",(consulta["nombre"],))
        
        respuesta=cursor.fetchall()
        if(0==len(respuesta)):#si la planta no existe se sube a la base de datos y se busca su imagen
            consulta["img"]=buscar_img([consulta["nombre"]]+consulta["alias"])#llamar al modulo de busqueda de iamgenes
            
            aliases= str(consulta["alias"]).replace("'", " ")# Escapar comillas simples'
            consulta["alias"]=aliases[1:len(aliases)-1]

            sql="INSERT INTO plantas (nombre_cientifico, nombres_comunes,humedad,temperatura,imagen) VALUES (%s, %s,0,0,%s);";
            values=(consulta["nombre"],consulta["alias"],consulta["img"])
            cursor.execute(sql,values)
            conexion.commit()
        else:
            consulta["img"]= respuesta[0][3]
            consulta["humedad"]=respuesta[0][4]
            consulta["temperatura"]=respuesta[0][5]
         
    os.remove(ruta_imagen)
    return render_template('planta.html',data=consulta)
    
# @app.route('/direccion/<campo_dinamico>/<int:numero>')
# def direccion(campo_dinamico):
#     data=campo_dinamico
#     return render_template("html.html",data=data)

@app.errorhandler(413)
def archivo_muy_grande(e):
    return "archivo muy pesado para el sistema"

if __name__=="__main__":
    app.run(debug=True)
