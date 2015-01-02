# -*- coding: utf8 -*-

from flask import Blueprint, render_template

index = Blueprint('index', __name__)

@index.route('/index', methods=['GET'])
def home():
    return render_template("index/index.html", username="hello world")