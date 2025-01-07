import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_page():
    response = client.post("/pages/", json={
        "title": "Home Page",
        "content": "Welcome to the home page."
    })
    assert response.status_code == 200
    assert response.json()["title"] == "Home Page"

def test_read_pages():
    response = client.get("/pages/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_page():
    response = client.get("/pages/1")  # Assuming page with ID 1 exists
    assert response.status_code == 200
    assert "title" in response.json()

def test_update_page():
    response = client.put("/pages/1", json={
        "content": "Updated content for the home page."
    })
    assert response.status_code == 200
    assert response.json()["content"] == "Updated content for the home page."

def test_delete_page():
    response = client.delete("/pages/1")  # Assuming page with ID 1 exists
    assert response.status_code == 200
    assert response.json()["message"] == "Page deleted"
