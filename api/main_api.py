import os
import time
from random import random, randint
from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify

from api.utils import api
from text_extract.clould_vision import detect_text

app = Flask(__name__)
app_api = Api(app)


class Employees(Resource):
    @api.beauty
    def get(self):
        a = 'Kẻ có'
        return {'a': a}


app_api.add_resource(Employees, '/test')  # Route_1

if __name__ == '__main__':
    app.run(port=8888, debug=True, passthrough_errors=True)
