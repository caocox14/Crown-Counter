import requests
import re

def obtener_imagen(plantas):
    """
    Función optimizada para Vercel. 
    Realiza una petición HTTP directa a PictureThisAI y extrae la imagen mediante 
    expresiones regulares, eliminando la necesidad de Selenium y navegadores pesados.
    """
    # Usamos un User-Agent para que la página crea que somos un navegador normal (como tu Firefox original)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0"
    }
    
    src = ['']
    
    for planta in plantas:
        # Tu misma lógica de formateo: "monstera deliciosa" -> "Monstera_deliciosa"
        nombre = planta.replace(" ", "_")
        if nombre:
            nombre = nombre[0].upper() + nombre[1:]
            
        url = f"https://www.picturethisai.com/es/wiki/{nombre}.html"
        print("Buscando imagen en PictureThisAI para la planta:", planta)
        
        try:
            # Hacemos la petición con un tiempo límite de 4 segundos para evitar congelar la página
            response = requests.get(url, headers=headers, timeout=4)
            
            if response.status_code == 200:
                # Buscamos la etiqueta img que tenga la clase 'description-main-image' en el HTML
                # Usamos una expresión regular simple para extraer el 'src' directamente
                match = re.search(r'class="[^"]*description-main-image[^"]*"[^>]*src="([^"]+)"', response.text)
                
                if match:
                    img_url = match.group(1)
                    src.append(img_url)
                    print(f"✅ ¡Imagen encontrada con éxito!: {img_url}")
                else:
                    print(f"⚠️ No se encontró la etiqueta con clase 'description-main-image' para: {planta}")
            else:
                print(f"❌ La página de PictureThis respondió con código: {response.status_code}")
                
        except Exception as e:
            print(f"Error al conectar con la enciclopedia para {planta}: {e}")
            pass

    # Tu misma lógica de retorno original
    if 1 < len(src):
        return src[1]  # primera imagen que se encontró
    return src[0]