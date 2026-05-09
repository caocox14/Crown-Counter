import requests
from consulta_img import obtener_imagen as oi

def identificar_planta(url,imagen,organ,project):
    print("identificar")
    API_KEY = "2b10hm5QUfNvomgsqb6c5F2we"
    PROJECT = project; # You can choose a more specific flora, see: /docs/newfloras
    api_endpoint = f"https://my-api.plantnet.org/v2/identify/{PROJECT}?api-key={API_KEY}"

    image_path = url+imagen
    image = open(image_path, 'rb')

    data = { 'organs': [organ] }

    files = [
        ('images', (image_path, image)),
    ]

    response = requests.post(api_endpoint, files=files, data=data)
    resultado = response.json()
    data=""
    print("verr", response.status_code)
    data={"nombre": "Indeterminado","certeza":0.0,"alias":"Ninguno","img":"https://static.wikia.nocookie.net/ficcion-sin-limites/images/5/57/Peashooter7.png/revision/latest/scale-to-width-down/250?cb=20210226142630&path-prefix=es"}
    if resultado.get("results") and response.status_code != 404:
        planta = resultado["results"][0]
        busquedas=[]

        data["nombre"]=planta["species"]["scientificNameWithoutAuthor"]
        data["alias"]=planta["species"]["commonNames"]
        data["certeza"]=planta["score"]
        
        busquedas= [data["nombre"]] + busquedas
        data["img"]=oi(busquedas)
    return data
