# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)


@app.route('/about', methods=['GET'])
def about():
    version = '0.1.0'
    return {
        'app_version': version
    }, 200
