# -*- coding: utf-8 -*-
from flask import (
    Flask,
    request,
    render_template,
    redirect,
    url_for)


import hashlib

# Creamos una instancia de Flask
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("main_window.html")


if __name__ == "__main__":
    app.run(debug=True)
