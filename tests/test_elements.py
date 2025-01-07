import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_element():
    response = client.post("/elements/", json={
        "type": "text",
        "content": "This is a text element.",
        "page_id": 1
    })
    assert response.status_code == 200
    assert response.json()["content"] == "This is a text element."

def test_read_elements():
    response = client.get("/elements/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_element():
    response = client.get("/elements/1")  # Assuming element with ID 1 exists
    assert response.status_code == 200
    assert "content" in response.json()

def test_update_element():
    response = client.put("/elements/1", json={
        "content": "Updated content for the text element."
    })
    assert response.status_code == 200
    assert response.json()["content"] == "Updated content for the text element."

def test_delete_element():
    response = client.delete("/elements/1")  # Assuming element with ID 1 exists
    assert response.status_code == 200
    assert response.json()["message"] == "Element deleted"
