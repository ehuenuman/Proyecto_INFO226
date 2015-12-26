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
    Retorna True si el usuario es encontrado en la base de datos
    """    
    conn = conectar()
    cursor = conn.cursor()
    sql = 'SELECT * FROM usuario WHERE user = "{}"'.format(usuario)
    cursor.execute(sql)
    if len(cursor.fetchall()) > 0:       
        return True
    else:    
        return False
    cursor.close()
