from flask import jsonify
from config import config
from models import db, User
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from requests import request
import spacy

# Cargar el modelo de SpaCy para el reconocimiento de entidades en español
nlp = spacy.load('es_core_news_sm')

enviroment = config['development']


def create_app(enviroment):
    app = Flask(__name__)

    app.config.from_object(enviroment)

    with app.app_context():
        db.init_app(app)
        db.create_all()

    return app

app = create_app(enviroment)

app.route('/api/v1/users', methods=['GET'])
def get_users():
    response = {'message': 'success'}
    return jsonify(response)

app.route('/api/v1/users/<id>', methods=['GET'])
def get_user(id):
    response = {'message': 'success'}
    return jsonify(response)

@app.route('/api/v1/users/', methods=['POST'])
def create_user():
    json = request.get_json(force=True)

    if json.get('username') is None:
        return jsonify({'message': 'Bad request'}), 400

    user = User.create(json['username'])

    return jsonify({'user': user.json() }) 

@app.route('/api/v1/users/<id>', methods=['PUT'])
def update_user(id):
    response = {'message': 'success'}
    return jsonify(response)

@app.route('/api/v1/users/<id>', methods=['DELETE'])
def delete_user(id):
    response = {'message': 'success'}
    return jsonify(response)

@app.route('/api/v1/users/ner', methods=['POST'])
def recognize_entities():
    try:
        data = request.json
        oraciones = data['oraciones']
        
        resultado = []
        for oracion in oraciones:
            doc = nlp(oracion)
            entidades = {}
            
            for ent in doc.ents:
                entidades[ent.text] = ent.label_
            
            resultado.append({
                "oraciones": oraciones,
                "entidades": entidades
            })
        
        return jsonify({"resultado": resultado})
    
    except Exception as e:
        return jsonify({"error": str(e)})

#IMPLEMENTACION DESARREGLADA CON HUGGINGFACE DE MEJOR MODELO DE NLP PARA LA TAREA EN MANO
#MUCHA MEJOR IMPLEMENTACION DEL MODELO PARA NLP-NER,BERT TIENE UNA PRECISION DE 99% EN GENERAL CUANDO SPACY SOLO EL 95% 
'''from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline

tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")

nlp = pipeline("ner", model=model, tokenizer=tokenizer)
example = "My name is Wolfgang and I live in Berlin"

ner_results = nlp(example)
print(ner_results)'''


if __name__ == '__main__':
    app.run(debug=True)
