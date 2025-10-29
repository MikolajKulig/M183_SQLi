from fastapi import FastAPI
from db import get_users, insert_user, update_user
from pydantic import BaseModel

app = FastAPI()

class UserCreate(BaseModel):
    first_name: str

class UserUpdate(BaseModel):
    user_id: int
    new_name: str


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

@app.put("/users")
def update_user_endpoint(payload: UserUpdate):
    update_user(payload.user_id, payload.new_name)
    return {"message": "User updated successfully"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
