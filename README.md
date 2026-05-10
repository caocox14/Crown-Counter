Requerimientos para correr proyecto
1.Instalar python
2.Instalar virtualenv (pip install virtualenv)
3. crear un entorno virtual en la carpeta de proyecto (python -m venv env)
4. prender el entorno virtual (source env/bin/activate)
5.Instalar las bibliotecas necesarias (pip install -r requirements.txt)
6. ejecutar el archivo app.py (python app.py)
-----En caso de descargar alguna libreria, por favor actualizar el archivo de requerimientos------

-----El aplicativo se actualizo para realizar busqueda de imagenes en linea
para evitar problemas es preferible realizar unos cambios en el archivo consulta_img (los cuales se indican en el mismo)
no son muchos y consiste en cambiar el buscador por defecto al que se use localmente.

---Se creo un archivo para replicar la base de datos, de postgre, se ejecuta automaticamente al iniciar app.py

----- Se requiere instalar NODE.JS para instalar poder correr Tailwind CSS, 1. entrar a la pagina de NODE.JS: https://nodejs.org/en/download
descargar la version v24.15.0, luego en la terminal del IDE posicionarse en la carpeta donde se encuentra el proyecto y aplicar este codigo: npm install, al correr este codigo debe asegurarse de verificar que en la carpeta del proyecto le aparezca otra carpeta llamada node_modules. con esto tendria instalado tailwind css, para luego activarlo y que detecte cambios y estilos debe aplicar el siguiente comando: npx tailwindcss -i ./static/css/input.css -o ./static/css/output.css --watch
con ese comando tailwind css estaria tomando los estilos y cambios que se quieran aplicar al front-end, pd: si se quiere estilizar, diseñar o cambiar alguna parte no tocar el archivo que se encuentra en static/css/output.css, tailwind toma el css/estilos de los parametros que se encuentran en "class" en el html y al guardar cambios los añade al output.css.
