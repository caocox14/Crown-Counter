from flask import Flask, render_template,request
from plantapi import identificar_planta as ip
from werkzeug.utils import secure_filename
import uuid
import os

app = Flask(__name__)

app.config['MAX_CONTENT_LENGTH'] = 20 * 1024 * 1024  # 20 MB

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/upload", methods=["POST"])
def upload():
    
    UPLOAD_FOLDER = "static/uploads/"#Folder de subida
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)#confirmacion 
    
    archivo = request.files["imagen"]#obtener imagen del campo del formulario "imagen"
    organ=request.form["organ"]#obtener 
    
    nombre_original = secure_filename(archivo.filename)
    _, extension = os.path.splitext(nombre_original)

    nuevo_nombre = str(uuid.uuid4())  # nombre único

    ruta_imagen = os.path.join(
        UPLOAD_FOLDER,
        nuevo_nombre + extension
    )

    archivo.save(ruta_imagen)
    print("archivo de entrada: ",nombre_original)
    data=ip(UPLOAD_FOLDER,nuevo_nombre + extension,organ,"all")
    
    return render_template('planta.html',data=data)
    
@app.route('/direccion/<campo_dinamico>/<int:numero>')
def direccion(campo_dinamico):
    data=campo_dinamico
    return render_template("html.html",data=data)

@app.errorhandler(413)
def archivo_muy_grande(e):
    return "archivo muy pesado para el sistema"

if __name__=="__main__":
    app.run(debug=True)
