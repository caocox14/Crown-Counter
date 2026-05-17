import requests
from consulta_img import obtener_imagen as oi
import json

def identificar_planta(imagenes,organ,project):
    print("Relizando peticiones al api")
    API_KEY = "2b10hm5QUfNvomgsqb6c5F2we"
    PROJECT = project; # You can choose a more specific flora, see: /docs/newfloras
    data={}
    datap = { 'organs': [] }
    files = []
    for direc in imagenes:
        image = open(direc, 'rb')
        files.append(('images', (direc, image)))
        datap['organs'].append(organ)
    api_endpoint = f"https://my-api.plantnet.org/v2/identify/{PROJECT}?api-key={API_KEY}"
    req = requests.Request('POST',url=api_endpoint, files=files, data=datap)
    preparar = req.prepare()

    s=requests.session()
    resultado=json.loads(s.send(preparar).text)
    print("lllego",resultado)
    try:#data de respuesta para plantas no encontradas
        if int(resultado["statusCode"]) in (400,404):
            data={"nombre": "Indeterminado","certeza":0.0,"alias":"Ninguno","img":"https://static.wikia.nocookie.net/ficcion-sin-limites/images/5/57/Peashooter7.png/revision/latest/scale-to-width-down/250?cb=20210226142630&path-prefix=es"}
    except KeyError as k:
        planta = resultado["results"][0]
        print("Resultado: ",planta)
        data["nombre"]=planta["species"]["scientificNameWithoutAuthor"]
        data["certeza"]=planta["score"]
        data["alias"]=planta["species"]["commonNames"]
        data["humedad"]=0
        data["temperatura"]=0
        data["img"]=''
    print("igualmente eso ocurre si :",data)
    return data
