import os
import psycopg2


def get_conn():
    """Stellt Verbindung zur Datenbank her"""
    # DB Passwort aus .env Datei lesen
    password = open('.env').read().split('=')[1].strip()

    return psycopg2.connect(
        dbname="m183",
        user="postgres",
        password=password,
        host="localhost",
        port="5432",
    )


def get_users():
    """Holt alle Benutzer aus der Datenbank"""
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, first_name FROM users;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [{"id": r[0], "first_name": r[1]} for r in rows]


def insert_user_0(first_name: str):
    """Fuegt neuen Benutzer ein - UNSICHER: SQL Injection moeglich!"""
    conn = get_conn()
    cur = conn.cursor()
    # ACHTUNG: Direkte String-Verkettung ist unsicher!
    cur.execute("INSERT INTO users (first_name) VALUES (\'" + first_name + "\')")
    conn.commit()
    cur.close()
    conn.close()


def get_users_by_id_0(user_id: int):
    """Holt Benutzer nach ID - UNSICHER: SQL Injection moeglich!"""
    conn = get_conn()
    cur = conn.cursor()

    # ACHTUNG: Direkte String-Verkettung ist unsicher!
    cur.execute("SELECT * FROM users WHERE id = " + str(user_id))
    
    user = cur.fetchone()
    
    cur.close()
    conn.close()
    
    return user
