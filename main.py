from fastapi import FastAPI
from db import get_users, get_users_by_id_0, insert_user_0
from gegenmassnahmen.massnahmen_2 import insert_user_2, get_users_by_id_2
from gegenmassnahmen.massnahmen_1 import insert_user_1, get_users_by_id_1
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
    insert_user_0(payload.first_name)
    return {"first_name": payload.first_name}

@app.post("/users-1", status_code=201)
def create_user_secure(payload: UserCreate):
    insert_user_1(payload.first_name)
    return {"first_name": payload.first_name}

@app.post("/users-2", status_code=201)
def create_user_secure(payload: UserCreate):
    insert_user_2(payload.first_name)
    return {"first_name": payload.first_name}

@app.get("/users/{user_id}")
def get_user_by_id(user_id: str):
    return get_users_by_id_0(user_id)

@app.get("/users-1/{user_id}")
def get_user_by_id(user_id: int):
    return get_users_by_id_1(user_id)

@app.get("/users-2/{user_id}")
def get_user_by_id(user_id: int):
    return get_users_by_id_2(user_id)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
