# -*- coding: utf-8 -*-
from flask import (
    request,
    render_template,
    redirect,
    url_for,
    jsonify)


from qti_interaction import app
import model


@app.route("/")
def index():
    return render_template("main_window.html")

@app.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
    return render_template('sign-up.html')

@app.route("/selec_multiple", methods=['GET', 'POST'])
def selec_multiple():
    return render_template('selec_multiple.html')

@app.route("/orden", methods=['GET', 'POST'])
def orden():
    return render_template('orden.html')

@app.route('/verifica_usuario')
def verifica_usuario():
	usuario = request.args.get('usuario', 0, type=str)	
	respuesta = model.verifica_usuario(usuario)
	return jsonify(result=respuesta)


if __name__ == "__main__":
    app.run(debug=True)
