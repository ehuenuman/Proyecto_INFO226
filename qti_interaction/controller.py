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
    print("Index")
    sumSessionCounter()
    if request.method == 'POST':
        print("POST")
        email = (request.form["email_login"]).encode('utf-8')
        password = (request.form["pass_login"]).encode('utf-8')
        print(email)
        print(password)
        email_erroneo = model.verifica_email(email)
        if email_erroneo is False:
            password_original = model.get_pass(email)
            if encrypt_pass(email, password) == password_original:
                session['name'] = model.get_name_user(email)
                session['user'] = email
                session['id_user'] = model.get_id_user(email)
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
        password = (request.form["password"]).encode('utf-8')
        password2 = (request.form["password2"]).encode('utf-8')

        exito = model.registrar_usuario(nombres,
                                        email,
                                        encrypt_pass(email,
                                                     password)
                                        )
        if exito:
            return render_template('main_window.html', error="201")
            # return redirect(url_for('index', error='201'))
        else:
            return render_template('sign-up.html', error="500")
    else:
        return render_template('sign-up.html')


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


@app.route("/seleccion-multiple/", methods=['GET', 'POST'])
def seleccion_multiple():
    return render_template('selec_multiple.html')


@app.route("/ordenamiento/", methods=['GET', 'POST'])
def ordenamiento():
    return render_template('orden.html')


@app.route("/terminos-pareados/", methods=['GET', 'POST'])
def terminos_pareados():
    return render_template('pareados.html')


@app.route("/completar-frase/", methods=['GET', 'POST'])
def completar_frase():
    return render_template('completar.html')


def sumSessionCounter():
    """
    Iniciara o incrementara un contador que guardara la variable de sesión.    
    """
    try:
        session['counter'] += 1
    except KeyError:
        session['counter'] = 1


def encrypt_pass(email, password):
    """
    Encripta la contraseña del usuario mediante hashlib, se utiliza sha224.
    En el proceso de encriptación se utiliza un salt personalizado para
    cada nuevo usuario.
    """
    if len(password) < len(email.split('@')[0]):
        end = len(password)
    else:
        end = len(email.split('@')[0])
    salt = ""
    for i in range(0, end):
        salt = "{}{}{}".format(salt, password[i], email[i])

    hash_pass = hashlib.sha224("{}{}{}".format(salt[0:len(salt) / 2].upper(),
                                               password,
                                               salt[len(salt) / 2: len(salt)])
                               ).hexdigest()
    return hash_pass
