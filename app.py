from flask import Flask, render_template,request
from plantapi import identificar_planta as ip
import os
from werkzeug.utils import secure_filename
import uuid
import json
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/upload", methods=["POST"])
def upload():
    
    UPLOAD_FOLDER = "static/uploads/"
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    
    archivo = request.files["imagen"]
    organ=request.form["organ"]
    caracteres=len(archivo.filename)
    
    if archivo.filename == "" or caracteres<5:
        return "No se seleccionó imagen"
    
    extension=archivo.filename[caracteres-4:caracteres]
    if extension != ".jpg" and extension != ".png":
        return f"No se seleccionó imagen ({extension})"
    
    nombre_original = secure_filename(archivo.filename)
    _, extension = os.path.splitext(nombre_original)

    nuevo_nombre = str(uuid.uuid4())  # nombre único

    ruta_imagen = os.path.join(
        UPLOAD_FOLDER,
        nuevo_nombre + extension
    )

    archivo.save(ruta_imagen)
    resultado=ip(UPLOAD_FOLDER,nuevo_nombre + extension,organ,"all")
    return f"IMAGEN DESCARGADA - resultado: {resultado} "

if __name__=="__main__":
    app.run(debug=True)
