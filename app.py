from flask import Flask, render_template,request
from plantapi import identificar_planta as ip
from werkzeug.utils import secure_filename
from consulta_img import obtener_mimagenes as om
import uuid
import os

app = Flask(__name__)

app.config['MAX_CONTENT_LENGTH'] = 20 * 1024 * 1024  # 20 MB

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/upload", methods=["POST"])
def upload():
    
    UPLOAD_FOLDER = "static/uploads/"
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    
    archivo = request.files["imagen"]
    organ=request.form["organ"]
    
    nombre_original = secure_filename(archivo.filename)
    _, extension = os.path.splitext(nombre_original)

    nuevo_nombre = str(uuid.uuid4())  # nombre único

    ruta_imagen = os.path.join(
        UPLOAD_FOLDER,
        nuevo_nombre + extension
    )

    archivo.save(ruta_imagen)
    data=ip(UPLOAD_FOLDER,nuevo_nombre + extension,organ,"all")
    if (data["nombre"]=="indeterminado"):
        return render_template('indeterminado.html')
    
    data["img"]=om(data["alias"])
    return render_template('planta.html',data=data)
    

@app.errorhandler(413)
def archivo_muy_grande(e):
    return "archivo muy pesado para el sistema"

if __name__=="__main__":
    app.run(debug=True)
