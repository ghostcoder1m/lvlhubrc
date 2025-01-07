import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_trigger():
    response = client.post("/triggers/", json={
        "workflow_id": 1,
        "type": "email_opened",
        "parameters": {"email": "test@example.com"},
        "schedule": "daily"
    })
    assert response.status_code == 200
    assert response.json()["type"] == "email_opened"

def test_read_triggers():
    response = client.get("/triggers/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_trigger():
    response = client.get("/triggers/1")  # Assuming trigger with ID 1 exists
    assert response.status_code == 200
    assert "type" in response.json()

def test_update_trigger():
    response = client.put("/triggers/1", json={
        "schedule": "weekly"
    })
    assert response.status_code == 200
    assert response.json()["schedule"] == "weekly"

def test_delete_trigger():
    response = client.delete("/triggers/1")  # Assuming trigger with ID 1 exists
    assert response.status_code == 200
    assert response.json()["message"] == "Trigger deleted"
