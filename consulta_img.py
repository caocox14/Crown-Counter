import requests
import re
from requests.exceptions import Timeout, ConnectionError

def obtener_imagen(plantas):
    """
    Función optimizada para Vercel. 
    Realiza una petición HTTP directa a PictureThisAI y extrae la imagen mediante 
    expresiones regulares, con timeouts y manejo de errores robusto.
    """
    # User-Agent para que la página crea que somos un navegador normal
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0"
    }
    
    src = ['']
    
    for planta in plantas:
        # Lógica de formateo: "monstera deliciosa" -> "Monstera_deliciosa"
        nombre = planta.replace(" ", "_")
        if nombre:
            nombre = nombre[0].upper() + nombre[1:]
            
        url = f"https://www.picturethisai.com/es/wiki/{nombre}.html"
        print(f"🔍 Buscando imagen en PictureThisAI para: {planta}")
        
        try:
            # ⏱️ TIMEOUT: 2 segundos máximo
            # Si la web externa es lenta, cortamos para no trabar la app
            print(f"   📡 GET {url} (timeout=2s)")
            response = requests.get(url, headers=headers, timeout=2)
            
            if response.status_code == 200:
                # Buscamos la etiqueta img con clase 'description-main-image'
                match = re.search(r'class="[^"]*description-main-image[^"]*"[^>]*src="([^"]+)"', response.text)
                
                if match:
                    img_url = match.group(1)
                    src.append(img_url)
                    print(f"   ✅ ¡Imagen encontrada!: {img_url[:60]}...")
                    return img_url  # Retornamos la primera que encuentras
                else:
                    print(f"   ⚠️ No se encontró etiqueta con clase 'description-main-image'")
            else:
                print(f"   ❌ PictureThis respondió con código {response.status_code}")
                
        except Timeout:
            print(f"   ⏱️ TIMEOUT: PictureThis tardó más de 2 segundos")
        except ConnectionError as e:
            print(f"   🌐 Error de conexión: {type(e).__name__}")
        except Exception as e:
            print(f"   ⚠️ Error buscando imagen: {type(e).__name__}: {str(e)[:50]}")
    
    # Si no se encontró nada, retornamos string vacío
    # app.py manejará esto con fallback a IMG_RESPALDO
    print(f"   ℹ️ No se encontró imagen, usando fallback")
    return ""