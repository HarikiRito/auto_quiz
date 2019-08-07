from flask import jsonify
import json


def beauty(func):
    def inner1(*args, **kwargs):
        res = func(*args, **kwargs)
        return jsonify(res)

    return inner1
