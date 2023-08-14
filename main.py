import spacy
from flask import jsonify, request, json
from spacy.lang.es.examples import sentences 

#Importar módulos propios
from app import create_app
from config import config

#Configuracción de variables de entorno
app = create_app(config)
nlp = spacy.load("es_core_news_sm")

@app.route('/')
def index():
    return jsonify({"message":"Prueba ML"})


@app.route('/oracion', methods=['POST'])
def process_sentence() -> json.Response:
    '''
    Realiza el proceso de reconocimiento de entidades nombradas y retorna cada una de
    estas con su etiqueta y la oración a la que pertenece.

        Parameters: 
            oraciones (json.Request): lista de oraciones.

        Returns:
            result (json.Response): JSON con la lista de oraciones 
                                    con sus respectivas entidades encontradas.
    '''
    list_of_sentences = request.json['oraciones']
    result = []

    for sentence in list_of_sentences:
        doc = nlp(sentence)
        #Dict comprenhension para iterar por todas las entidades, obtener su texto y su etiqueta.
        entities = {ent.text:ent.label_ for ent in doc.ents}
        if len(entities) == 0:
            entities = "Entidades no encontradas"
        result.append({"oración":sentence, "entidades":entities})

    return jsonify({"resultado":result})


if __name__ == '__main__':
    app.run(debug=True, port=4000)