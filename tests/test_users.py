import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={
        "email": "test@example.com",
        "first_name": "Test",
        "last_name": "User",
        "company": "Test Company",
        "password": "securepassword"
    })
    assert response.status_code == 200
    assert response.json()["email"] == "test@example.com"

def test_read_users():
    response = client.get("/users/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_user():
    response = client.get("/users/1")
    assert response.status_code == 404  # Assuming user with ID 1 does not exist

def test_update_user():
    response = client.put("/users/1", json={
        "first_name": "Updated",
        "last_name": "User"
    })
    assert response.status_code == 404  # Assuming user with ID 1 does not exist

def test_delete_user():
    response = client.delete("/users/1")
    assert response.status_code == 404  # Assuming user with ID 1 does not exist
