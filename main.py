from fastapi import FastAPI
from db import get_users

app = FastAPI()

@app.get("/test")
def helloWorld():
    return "Hello world"

@app.get("/users")
def getUsers():
    return get_users()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
