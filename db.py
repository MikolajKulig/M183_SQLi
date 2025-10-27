import os
import psycopg2


def get_conn():
    # Keep DB name/user/host/port hard-coded as before, but read the password
    # from the environment variable DB_PASSWORD if present.
    password = os.environ.get("DB_PASSWORD")
    return psycopg2.connect(
        dbname="m183",
        user="postgres",
        password=password,
        host="localhost",
        port="5432",
    )

def get_users():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, first_name FROM users;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [{"id": r[0], "name": r[1]} for r in rows]

def insert_user(first_name: str):

    conn = get_conn()
    cur = conn.cursor()

    cur.execute(f"INSERT INTO users (first_name) VALUES (\'{first_name}\')")

    conn.commit()  
    cur.close()
    conn.close()
