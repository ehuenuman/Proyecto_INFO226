# -*- coding: utf-8 -*-
from flask import (
    request,
    render_template,
    redirect,
    url_for,
    jsonify)

from qti_interaction import app
import hashlib
import model


@app.route("/")
def index():
    return render_template("main_window.html")


@app.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
    if request.method == "POST":
        print("POST")
        nombres = (request.form["nombres"]).encode('utf-8')
        email = (request.form["email"]).encode('utf-8')
        usuario = (request.form["usuario"]).encode('utf-8')
        password = (request.form["password"]).encode('utf-8')
        password2 = (request.form["password2"]).encode('utf-8')

        exito = model.registrar_usuario(nombres,
                                        email,
                                        usuario,
                                        encrypt_pass(usuario,
                                                     email,
                                                     password)
                                        )
        if exito:        
            return render_template('main_window.html', error="201")
        else:
            pass
    else:
        print("GET")
        return render_template('sign-up.html')


@app.route('/verifica_usuario')
def verifica_usuario():
    usuario = request.args.get('usuario')
    respuesta = model.verifica_usuario(usuario)
    return jsonify(result=respuesta)


@app.route('/verifica_email')
def verifica_email():
    email = request.args.get('email')
    respuesta = model.verifica_email(email)
    return jsonify(result=respuesta)


def encrypt_pass(usuario, email, password):
    """
    Encripta la contraseña del usuario mediante hashlib, se utiliza sha224.
    En el proceso de encriptación se utiliza un salt personalizado para
    cada nuevo usuario.
    """
    if len(usuario) < len(email.split('@')[0]):
        end = len(usuario)
    else:
        end = len(email.split('@')[0])
    salt = ""
    for i in range(0, end):
        salt = "{}{}{}".format(salt, usuario[i], email[i])

    hash_pass = hashlib.sha224("{}{}{}".format(salt[0:len(salt) / 2].upper(),
                                               password,
                                               salt[len(salt) / 2: len(salt)])
                               ).hexdigest()
    return hash_pass
