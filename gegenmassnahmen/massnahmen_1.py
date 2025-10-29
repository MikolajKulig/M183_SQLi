from db import insert_user_0, get_users_by_id_0

def insert_user_1(first_name: str):
    if not first_name or not isinstance(first_name, str):
        raise ValueError("First name must be a non-empty string")
    
    if not all(c.isalpha() or c.isspace() or c in ".-'" for c in first_name):
        raise ValueError("First name contains invalid characters")
    
    if len(first_name) > 50:
        raise ValueError("First name too long")
    
    insert_user_0(first_name)

def get_users_by_id_1(user_id: int):
    if not isinstance(user_id, int):
        raise ValueError("User ID must be an integer")
    
    if user_id <= 0:
        raise ValueError("User ID must be a positive integer")
    
    return get_users_by_id_0(user_id)