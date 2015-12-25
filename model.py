# -*- coding: utf-8 -*-
import MySQLdb

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASS = ''

def conectar():
    conn = MySQLdb.connect(DB_HOST, DB_USER, DB_PASS)
    cursor = conn.cursor()
    cursor.execute('use qti_interaction;')
    return conn