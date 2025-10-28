from fastapi import FastAPI
from db import get_users, insert_user
from gegenmassnahmen.mittel_komplex import insert_user_secure
from pydantic import BaseModel

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


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
