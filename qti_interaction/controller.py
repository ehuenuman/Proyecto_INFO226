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

@app.route("/seleccion-multiple", methods=['GET', 'POST'])
def seleccion_multiple():
    return render_template('selec_multiple.html')

@app.route("/ordenamiento", methods=['GET', 'POST'])
def ordenamiento():
    return render_template('orden.html')

@app.route("/terminos-pareados", methods=['GET', 'POST'])
def terminos_pareados():
    return render_template('pareados.html')

@app.route('/verifica_usuario')
def verifica_usuario():
	usuario = request.args.get('usuario', 0, type=str)	
	respuesta = model.verifica_usuario(usuario)
	return jsonify(result=respuesta)


if __name__ == "__main__":
    app.run(debug=True)
