from db import get_conn

def insert_user_secure(first_name: str):
    conn = get_conn()
    cur = conn.cursor()
    SQL_TEMPLATE = "INSERT INTO users (first_name) VALUES (%s)"
    
    cur.execute(SQL_TEMPLATE, (first_name,))
    
    conn.commit()  
    cur.close()
    conn.close()
