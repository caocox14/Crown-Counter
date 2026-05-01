import requests
from bs4 import BeautifulSoup

def obtener_imagen_inaturalist(nombre):
    url = "https://api.inaturalist.org/v1/taxa"

    params = {
        "q": nombre,
        "limit": 1
    }

    response = requests.get(url)
    data = response.json()

    if data["results"]:
        taxon = data["results"][0]
        return taxon.get("default_photo", {}).get("medium_url")

    return None
def obtener_mimagenes(alias):
    resultado =[]
    for al in alias:
        resultado.append(obtener_imagen_inaturalist(al))
    return resultado[0]
