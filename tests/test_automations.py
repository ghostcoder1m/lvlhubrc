import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_automation():
    response = client.post("/automations/", json={
        "name": "Email Automation",
        "description": "An automation for sending emails."
    })
    assert response.status_code == 200
    assert response.json()["name"] == "Email Automation"

def test_read_automations():
    response = client.get("/automations/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_automation():
    response = client.get("/automations/1")  # Assuming automation with ID 1 exists
    assert response.status_code == 200
    assert "name" in response.json()

def test_update_automation():
    response = client.put("/automations/1", json={
        "description": "Updated automation description."
    })
    assert response.status_code == 200
    assert response.json()["description"] == "Updated automation description."

def test_delete_automation():
    response = client.delete("/automations/1")  # Assuming automation with ID 1 exists
    assert response.status_code == 200
    assert response.json()["message"] == "Automation deleted"
