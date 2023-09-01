from flask import jsonify
from config import config
from models import db, User
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from requests import request

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

if __name__ == '__main__':
    app.run(debug=True)