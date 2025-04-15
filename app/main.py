from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello world"}

@app.get("/ping")
def ping():
    return {"message": "This is pong"}

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello, {name}!"}
