import requests
import json
import os

def identificar_planta(imagenes, organ, project):
    """
    Identifica plantas usando PlantNet API con timeouts y reintentos
    """
    print("🔍 Realizando peticiones a la API de PlantNet...")
    
    # API KEY desde variable de entorno o valor por defecto (CAMBIAR ANTES DE PRODUCCIÓN)
    API_KEY = os.environ.get("PLANTNET_API_KEY", "2b10hm5QUfNvomgsqb6c5F2we")
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
            print(f"❌ Error al abrir la imagen {direc}: {e}")
            return data

    api_endpoint = f"https://my-api.plantnet.org/v2/identify/{PROJECT}?api-key={API_KEY}"
    
    try:
        # ⏱️ TIMEOUT: 25 segundos máximo para PlantNet (es una API externa lenta a veces)
        print("📤 Enviando petición a PlantNet con timeout=25s...")
        response = requests.post(api_endpoint, files=files, data=datap, timeout=25)
        
        # IMPORTANTE: Cerrar los archivos en memoria obligatoriamente
        for f in files:
            try:
                f[1][1].close()
            except:
                pass
        
        # Validar que la respuesta sea exitosa
        if response.status_code != 200:
            print(f"⚠️ PlantNet respondió con código {response.status_code}")
            return data
            
        resultado = response.json()
        
        # Validamos si la API retornó un error o statusCode de no encontrado
        if "statusCode" in resultado and int(resultado["statusCode"]) in (400, 404):
            print(f"⚠️ PlantNet retornó statusCode {resultado['statusCode']}")
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
            
            print(f"✅ Planta identificada: {data['nombre']} (certeza: {certeza_porcentaje}%)")
        else:
            print("⚠️ PlantNet no encontró resultados")
            
    except requests.Timeout:
        print("❌ TIMEOUT: PlantNet tardó más de 25 segundos")
        return data
    except requests.ConnectionError as e:
        print(f"❌ Error de conexión a PlantNet: {e}")
        return data
    except Exception as e:
        print(f"❌ Error crítico en comunicación con PlantNet: {type(e).__name__}: {e}")
        return data
        
    return data