import os
import psycopg2


def get_conn():
    # Read the DB password from the environment. No hard-coded default.
    password = os.environ.get("DB_PASSWORD")
    if not password:
        raise RuntimeError("DB_PASSWORD is not set; set it in the environment.")

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
