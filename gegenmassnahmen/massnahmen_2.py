from db import get_conn

def insert_user_2(first_name: str):
    conn = get_conn()
    cur = conn.cursor()
    sql = "INSERT INTO users (first_name) VALUES (%s)"
    
    cur.execute(sql, (first_name,))
    
    conn.commit()  
    cur.close()
    conn.close()

def get_users_by_id_2(user_id: int):
    conn = get_conn()
    cur = conn.cursor()
    sql = "SELECT * FROM users WHERE id = (%s)"
    cur.execute(sql, (user_id,))
    
    user = cur.fetchone()
    
    cur.close()
    conn.close()
    
    return user
