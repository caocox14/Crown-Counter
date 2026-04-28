from flask import Flask, render_template,request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/upload", methods=["POST"])
def upload():
    
    UPLOAD_FOLDER = "static/uploads"
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    
    archivo = request.files["imagen"]

    if archivo.filename == "":
        return "No se seleccionó imagen"

    # Guardar imagen recibida
    ruta_imagen = os.path.join(
        UPLOAD_FOLDER,
        archivo.filename
    )

    archivo.save(ruta_imagen)

    return "IMAGEN DESCARGADA"

if __name__=="__main__":
    app.run(debug=True)
