import requests
import json

def identificar_planta(imagenes, organ, project):
    print("Realizando peticiones a la API de PlantNet...")
    API_KEY = "2b10hm5QUfNvomgsqb6c5F2we"
    PROJECT = project
    
    # Estructura base de retorno por defecto
    data = {
        "nombre": "Indeterminado",
        "certeza": 0,
        "alias": "Ninguno",
        "img": ""
    }
    
    files = []
    datap = { 'organs': [] }
    
    # Abrimos los archivos de imagen de manera segura
    for direc in imagenes:
        try:
            image = open(direc, 'rb')
            files.append(('images', (direc, image)))
            datap['organs'].append(organ)
        except Exception as e:
            print(f"Error al abrir la imagen {direc}: {e}")
            return data

    api_endpoint = f"https://my-api.plantnet.org/v2/identify/{PROJECT}?api-key={API_KEY}"
    
    try:
        # Petición directa y limpia
        response = requests.post(api_endpoint, files=files, data=datap)
        
        # IMPORTANTE: Cerrar los archivos en memoria obligatoriamente
        for f in files:
            f[1][1].close()
            
        resultado = response.json()
        
        # Validamos si la API retornó un error o statusCode de no encontrado
        if "statusCode" in resultado and int(resultado["statusCode"]) in (400, 404):
            return data
            
        if "results" in resultado and len(resultado["results"]) > 0:
            planta = resultado["results"][0]
            
            # Procesamos los nombres comunes para enviarlos como un String limpio separado por comas
            nombres_comunes = planta["species"].get("commonNames", [])
            alias_limpio = ", ".join(nombres_comunes[:2]) if nombres_comunes else "Ninguno"
            
            # Multiplicamos el score (0.85 -> 85) para mandarlo como entero listo al Frontend
            certeza_porcentaje = round(planta.get("score", 0.0) * 100)
            
            data["nombre"] = planta["species"].get("scientificNameWithoutAuthor", "Indeterminado")
            data["certeza"] = certeza_porcentaje
            data["alias"] = alias_limpio
            data["humedad"] = 0
            data["temperatura"] = 0
            data["img"] = ''
            
    except Exception as e:
        print("Error crítico en la comunicación con PlantNet:", e)
        
    return data