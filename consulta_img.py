from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException as ex1
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options #cambiar aqui por el navegador a utilizar ej:
# from selenium.webdriver.chrome.options import Options

def obtener_imagen(plantas):#esta funcion se encarga de buscar la imagen relacionada a la planta que se identifico, para que asi el usuario pueda compararla visualmente y asegurarse
    options = Options()
    options.add_argument("--headless")  # 👈 clave, si es clave

    driver = webdriver.Firefox(options=options) #cambiar aqui por el navegar que se utilize prereriblemente chrome - esta probado que con firefoz funciona
    #driver = webdriver.Chrome(options=options)
    src=["https://png.pngtree.com/png-clipart/20230405/original/pngtree-question-mark-icon-png-image_9025635.png"]
    
    for planta in plantas:#busqueda de los y nombre cientifico
        nombre = planta.replace(" ", "_")
        nombre=nombre[0].upper()+nombre[1:len(nombre)]
        url = f"https://www.picturethisai.com/es/wiki/{nombre}.html"#la imagen se extrae de esta pagina
        print("Buscando imagen para la planta: ",planta)
        try:
            driver.get(url)
            img = driver.find_element(By.CLASS_NAME, "description-main-image")
            src.append(img.get_attribute("src"))
        except ex1 as e:
            print("No se encontró la imagen para la planta: ",planta, ": ",e.msg)
            pass
    driver.quit()
    if 1<len(src):#en caso que no se encuentre la imagen se muestra un indicador que haga referencia
        return src[1]#primera imagen que se encontro
    return src[0]