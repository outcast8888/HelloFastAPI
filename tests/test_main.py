from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello world"}

def test_ping():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"message": "pong second time"}

def test_hello_name():
    response = client.get("/hello/Alex")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, Alex!"}
