# -*- coding: utf-8 -*-
import MySQLdb

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASS = ''


def conectar():
    """Crea la conexión a la base de datos"""
    conn = MySQLdb.connect(DB_HOST, DB_USER, DB_PASS)
    cursor = conn.cursor()
    cursor.execute('use qti_interaction;')
    return conn


def verifica_usuario(usuario):
    """
    Realiza la consulta por un usuario en especifico.
    Retorna True si el usuario esta disponible para ser usado.
    """
    conn = conectar()
    cursor = conn.cursor()
    sql = 'SELECT * FROM usuario WHERE user = "{}"'.format(usuario)
    cursor.execute(sql)
    if len(cursor.fetchall()) > 0:
        cursor.close()
        return False
    else:
        cursor.close()
        return True


def verifica_email(email):
    """
    Realiza la consulta por un correo en especifico.
    Retorna True si el correo no esta registrado en la BD.
    """
    conn = conectar()
    cursor = conn.cursor()
    sql = 'SELECT * FROM usuario WHERE email = "{}"'.format(email)
    cursor.execute(sql)
    if len(cursor.fetchall()) > 0:
        cursor.close()
        return False
    else:
        cursor.close()
        return True


def registrar_usuario(nombres, email, usuario, password):
    """
    Ingresa un nuevo usuario a la base de datos.
    Retorna True si la operación se realizo con exito.
    """
    conn = conectar()
    cursor = conn.cursor()

    sql = 'INSERT INTO usuario(nombre_completo, email, user, password) '
    sql += 'VALUES ("{}","{}","{}","{}")'.format((nombres),
                                                 (email),
                                                 (usuario),
                                                 (password)
                                                )
    try:
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        return True
    except MySQLdb.Error as e:
        print "Error al añadir nuevo usuario:", e.args[0]
        cursor.close()
        return False
