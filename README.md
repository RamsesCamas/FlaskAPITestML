# Prueba técnica con Flask

### Ejecutar proyecto
Para ejecutar el proyecto primero es necesario crear un entorno virtual con la herramienta de su preferencia y activarlo.

Por ejemplo:
```
python -m venv env

source env/bin/activate
```

Posteriormente se deben instalar las dependencias con el comando
```
pip install -r requirements.txt
```

Una vez instaladas las dependencias dentro del entorno virtual se instalará el modelo de Spacy para Name Entity Recognition (NER), con el siguiente comando:
```
spacy download es_core_news_sm
```

Ahora si, es momento de ejecutar el proyecto, ejecutando el archivo **main.py**
Por ejemplo:
```
python main.py
```

### Hacer peticiones a la API

En su herramienta de preferencia, en mi caso Postman, acceda al endpoint **/oracion** para realizar la petición **POST**, la cuál enviará un JSON conteniendo una lista de oraciones.

Endpoint ejecutandose localmente
```
http://127.0.0.1:4000/oracion
```

En la siguiente imagen se muestra un ejemplo usando Postman
![Usando Postman](/images/postman_flask.png)
