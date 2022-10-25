from flask_app import app
from api.elastic_test import connect_elasticsearch
from flask import jsonify, request
from elasticsearch import RequestsHttpConnection

es = connect_elasticsearch()

@app.route('/', methods=['GET'])
def home():
    message = 'Flask is UP and RUNNING'
    return jsonify(message)

@app.route('/get_data', methods=['GET'])
def get_data():
    try:
        results = es.get(index='my-index', id=1)
        return jsonify(results['_source']['text'])
    except:
        return jsonify("There is no data")