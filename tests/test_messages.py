import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_message():
    response = client.post("/messages/", json={
        "content": "Hello, this is a test message.",
        "sender_id": 1,
        "recipient_id": 2
    })
    assert response.status_code == 200
    assert response.json()["content"] == "Hello, this is a test message."

def test_read_messages():
    response = client.get("/messages/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_message():
    response = client.get("/messages/1")  # Assuming message with ID 1 exists
    assert response.status_code == 200
    assert "content" in response.json()

def test_update_message():
    response = client.put("/messages/1", json={
        "content": "Updated message content."
    })
    assert response.status_code == 200
    assert response.json()["content"] == "Updated message content."

def test_delete_message():
    response = client.delete("/messages/1")  # Assuming message with ID 1 exists
    assert response.status_code == 200
    assert response.json()["message"] == "Message deleted"
