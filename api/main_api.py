import os
import time
from random import random, randint

from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify

from text_extract.clould_vision import detect_text

app = Flask(__name__)
api = Api(app)


class Employees(Resource):
    def get(self):
        a = randint(1, 1000)
        time.sleep(1)
        return {'a': a}


api.add_resource(Employees, '/test')  # Route_1

if __name__ == '__main__':
    app.run(port=8888)
