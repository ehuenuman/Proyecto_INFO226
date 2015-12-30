# -*- coding: utf-8 -*-
import MySQLdb

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASS = ''


def conectar():
    """Crea la conexión a la base de datos"""
    conn = MySQLdb.connect(DB_HOST, DB_USER, DB_PASS, charset='utf8')
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


def get_email_pass(usuario):
    """
    Obtiene el email y el pass de un usuario en especifico.
    Se asume que el usuario existe en la base de datos, es por ello que
    primero se debe de validar el usuario con el metodo verifica_usuario.
    """
    conn = conectar()
    cursor = conn.cursor()
    sql = 'SELECT email, password FROM usuario WHERE user = "{}"'.format(
        usuario)
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    return data


def get_id_user(usuario):
    """
    Obtiene el registro id de un usuario especifico.
    Se asume que el usuario existe en la base de datos, es por ello que primero
    se debe de validar el usuario con el metodo verifica_usuario.
    """
    conn = conectar()
    cursor = conn.cursor()
    sql = 'SELECT id FROM usuario WHERE user = "{}"'.format(usuario)
    cursor.execute(sql)
    id_usuario = cursor.fetchall()
    cursor.close()
    return id_usuario[0][0]


def get_preguntas(id_user=None):
    """
    Obtiene las ultimas tres preguntas añadidas por un usuario en especifico.
    """
    conn = conectar()
    cursor = conn.cursor()
    if id_user != None:
        sql = 'SELECT id, enunciado, tipo, fecha FROM pregunta '
        sql += 'WHERE usuario_id={} '.format(id_user)
        sql += 'order by id DESC LIMIT 3'
        cursor.execute(sql)
        respuesta = cursor.fetchall()
        cursor.close()
        preguntas = {"pregunta": []}        
        for i in range(0,3):
            preguntas["pregunta"].append({"id": respuesta[i][0], "enunciado": respuesta[i][1], "tipo": respuesta[i][2], "fecha": str(respuesta[i][3])})       
    else:
        sql = 'SELECT pr.id, pr.enunciado, pr.tipo, pr.fecha, us.nombre_completo'
        sql += ' FROM pregunta pr, usuario us'
        sql += ' WHERE pr.usuario_id = us.id order by pr.id DESC LIMIT 4'
        cursor.execute(sql)
        respuesta = cursor.fetchall()
        cursor.close()
        preguntas = {"pregunta": []}        
        for i in range(0,4):
            preguntas["pregunta"].append({"id": respuesta[i][0], "enunciado": respuesta[i][1], "tipo": respuesta[i][2], "fecha": str(respuesta[i][3]), "autor": respuesta[i][4]})

    print(preguntas["pregunta"])
    return preguntas["pregunta"]

if __name__ == "__main__":
    get_preguntas()
