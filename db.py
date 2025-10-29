import os
import psycopg2


def get_conn():
    # Read DB password from the environment. No hard-coded default.
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
    return [{"id": r[0], "first_name": r[1]} for r in rows]


def insert_user(first_name: str):
    conn = get_conn()
    cur = conn.cursor()
    # Use parameterized query to avoid SQL injection
    cur.execute("INSERT INTO users (first_name) VALUES (%s)", (first_name,))
    conn.commit()
    cur.close()
    conn.close()


def get_users_by_name_vulnerable(name: str):

    conn = get_conn()
    cur = conn.cursor()
    # Vulnerable: direct string interpolation
    query = f"SELECT id, first_name FROM users WHERE first_name = '{name}';"
    cur.execute(query)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [{"id": r[0], "first_name": r[1]} for r in rows]
