from fastapi import FastAPI
from db import get_users, insert_user, get_users_by_name_vulnerable
from gegenmassnahmen.mittel_komplex import insert_user_secure
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class UserCreate(BaseModel):
    first_name: str


@app.get("/test")
def helloWorld():
    return "Hello world"

@app.get("/users")
def getUsers():
    return get_users()

@app.post("/users", status_code=201)
def create_user(payload: UserCreate):
    insert_user(payload.first_name)
    return {"first_name": payload.first_name}

@app.post("/users-secure", status_code=201)
def create_user_secure(payload: UserCreate):
    insert_user_secure(payload.first_name)
    return {"first_name": payload.first_name}


@app.get("/vuln_users")
def vuln_get_users(name: Optional[str] = ""):
    """Vulnerable endpoint for demonstration of SQL injection (2.1 confidentiality).
    Query parameter: name. This endpoint intentionally forwards the raw value
    into a concatenated SQL statement (see `db.get_users_by_name_vulnerable`).
    """
    return get_users_by_name_vulnerable(name)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
