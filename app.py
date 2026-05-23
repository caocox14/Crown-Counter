from flask import Flask, render_template, request, jsonify
from plantapi import identificar_planta as api
from consulta_img import obtener_imagen as buscar_img
from conexion_base import get_connection, verificar_tabla 
from werkzeug.utils import secure_filename
import uuid
import os

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 20 * 1024 * 1024  # 20 MB

@app.route('/')
def index():
    # ⚡ ¡Ahora carga al instante! Eliminamos verificar_tabla() de aquí
    # para que Vercel entregue el HTML en milisegundos sin consultar la DB.
    return render_template('index.html')

@app.route("/upload", methods=["POST"])
def upload():
    imagenes = request.files.getlist("imagen")
    imagenes_n = []
    
    # 💡 En Vercel, el único directorio con permisos de escritura real es '/tmp'
    ruta_temporal = '/tmp/uploads'
    if not os.path.exists(ruta_temporal):
        try:
            os.makedirs(ruta_temporal)
        except Exception as e:
            print("Aviso creando carpeta temporal:", e)
    
    for imagen in imagenes:
        if imagen.filename == '':
            continue
        _, extension = os.path.splitext(secure_filename(imagen.filename))
        # Guardamos de forma segura en el almacenamiento volátil del servidor
        ruta_imagen = f"{ruta_temporal}/{str(uuid.uuid4())}{extension}"
        imagen.save(ruta_imagen)
        imagenes_n.append(ruta_imagen)
        
    if not imagenes_n:
        return jsonify({"nombre": "Indeterminado", "alias": "Ninguno", "certeza": 0}), 400
    
    consulta = api(imagenes_n, "auto", "all")
    
    for ruta in imagenes_n:
        if os.path.exists(ruta):
            os.remove(ruta)
            
    resultado_final = procesar_peticion(consulta)
    return jsonify(resultado_final)
    
def procesar_peticion(consulta):
    if consulta["nombre"] != "Indeterminado":
        conexion = get_connection()
        if conexion is None:
            print("❌ No se pudo establecer conexión con Supabase en esta petición.")
            return consulta
            
        try:
            cursor = conexion.cursor()
            
            cursor.execute("SELECT imagen, humedad, temperatura FROM public.plantas WHERE nombre_cientifico = %s;", (consulta["nombre"],))
            respuesta = cursor.fetchall()
            
            if len(respuesta) == 0:
                print(f"Planta nueva detectada: {consulta['nombre']}. Buscando imagen...")
                terminos_busqueda = [consulta["nombre"]]
                if consulta["alias"] != "Ninguno":
                    terminos_busqueda.append(consulta["alias"])
                
                try:
                    consulta["img"] = buscar_img(terminos_busqueda)
                except Exception as err_img:
                    print("Error al buscar imagen en la web:", err_img)
                    consulta["img"] = ""
                    
                try:
                    sql = "INSERT INTO public.plantas (nombre_cientifico, nombres_comunes, humedad, temperatura, imagen) VALUES (%s, %s, 0, 0, %s);"
                    values = (consulta["nombre"], consulta["alias"], consulta["img"])
                    cursor.execute(sql, values)
                    conexion.commit()
                    print("Planta guardada con éxito en Supabase.")
                except Exception as err_db:
                    conexion.rollback()
                    print("Error al insertar en Supabase, haciendo rollback:", err_db)
            else:
                print("Planta encontrada en Supabase. Recuperando registros...")
                consulta["img"] = respuesta[0][0]          
                consulta["humedad"] = respuesta[0][1]      
                consulta["temperatura"] = respuesta[0][2]  

            cursor.close()
        except Exception as e:
            print("Error procesando la consulta SQL:", e)
        finally:
            conexion.close()

    if not consulta.get("img") or consulta["img"] == '':
        consulta["img"] = 'https://png.pngtree.com/png-clipart/20230405/original/pngtree-question-mark-icon-png-image_9025635.png'
        
    return consulta

@app.errorhandler(413)
def archivo_muy_grande(e):
    return jsonify({"nombre": "Indeterminado", "error": "Archivo muy pesado para el sistema"}), 413

if __name__ == "__main__":
    app.run(debug=True)