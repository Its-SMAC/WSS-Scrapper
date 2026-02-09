"""
Markets:
    'A' = Auchan
    'C' = Continente
    'P' = Pingo doce
"""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Home Page"


@app.route("/status")
def status():
    return "Api was working"
