import psycopg2

def get_conn():
    return psycopg2.connect(
        dbname="m183",
        user="postgres",
        password="mysecretpassword",
        host="localhost",
        port="5432"
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

def get_users_by_id(user_id: int):
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("SELECT * FROM users WHERE id = " + user_id)
    
    user = cur.fetchone()
    
    cur.close()
    conn.close()
    
    return user