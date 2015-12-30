# -*- coding: utf-8 -*-
from flask import (
    request,
    render_template,
    redirect,
    url_for,
    jsonify,
    session)

from qti_interaction import app
import hashlib
import model


@app.route("/", methods=['GET', 'POST'])
def index():
    sumSessionCounter()
    if request.method == 'POST':
        usuario = (request.form["user_login"]).encode('utf-8')
        password = (request.form["pass_login"]).encode('utf-8')

        existe_usuario = model.verifica_usuario(usuario)
        if existe_usuario is False:
            print("Usuario correcto")
            data = model.get_email_pass(usuario)
            if encrypt_pass(usuario, data[0][0], password) == data[0][1]:
                print ("Password Correcta")
                session['user'] = usuario
                session['id_user'] = model.get_id_user(usuario)

                # return render_template("main_window.html", user=usuario)
                return redirect(url_for('index'))

        return render_template("main_window.html", error="401")

    else:  # GET Method
        return render_template("main_window.html")


@app.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
    if request.method == "POST":
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
            # return redirect(url_for('index', error='201'))
        else:
            return render_template('sign-up.html', error="500")
    else:
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

@app.route('/get_preguntas')
def get_preguntas():
    id_user = request.args.get('id_usuario')
    preguntas = model.get_preguntas(id_user)
    return jsonify(preguntas=preguntas)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


def sumSessionCounter():
    """
    Iniciara o incrementara un contador que guardara la variable de sesión.    
    """
    try:
        session['counter'] += 1
    except KeyError:
        session['counter'] = 1


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
