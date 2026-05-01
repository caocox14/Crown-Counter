import json, requests

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
    if resultado.get("results") and response.status_code != 404:
        planta = resultado["results"][0]

        nombre = planta["species"]["scientificNameWithoutAuthor"]
        alias = planta["species"]["commonNames"]
        certeza = planta["score"]
        
        data={"nombre": nombre,"certeza": certeza,"alias":alias}
    else:
        data={"nombre": "Indeterminado","certeza":0.0,"alias":"Ninguno"}
    return data
