import json, requests

def identificar_planta(url,imagen,organ,project):
    API_KEY = "2b10hm5QUfNvomgsqb6c5F2we"
    PROJECT = project; # You can choose a more specific flora, see: /docs/newfloras
    api_endpoint = f"https://my-api.plantnet.org/v2/identify/{PROJECT}?api-key={API_KEY}"

    image_path = url+imagen
    image = open(image_path, 'rb')

    data = { 'organs': [organ] }

    files = [
        ('images', (image_path, image)),
    ]

    req = requests.Request('POST', url=api_endpoint, files=files, data=data)
    prepared = req.prepare()
    s = requests.Session()
    response = s.send(prepared)
    json_result = json.loads(response.text)

    if(response.status_code==200):
        print("Busqueda exitosa!")
        planta = json_result["results"][0]
        nombre = planta["species"]["scientificNameWithoutAuthor"]
        confianza = planta["score"]
        data={"planta": nombre,"confianza":confianza,"estado":True}
        return data
    else:
        data={"response":response.status_code,"estado":False}
        return data
