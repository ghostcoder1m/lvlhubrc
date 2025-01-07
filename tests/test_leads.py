import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_lead():
    response = client.post("/leads/", json={
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "phone": "1234567890",
        "status": "New",
        "source": "Web Form",
        "owner_id": 1
    })
    assert response.status_code == 200
    assert response.json()["email"] == "john.doe@example.com"

def test_read_leads():
    response = client.get("/leads/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_lead():
    response = client.get("/leads/1")  # Assuming lead with ID 1 exists
    assert response.status_code == 200
    assert "email" in response.json()

def test_update_lead():
    response = client.put("/leads/1", json={
        "status": "Contacted"
    })
    assert response.status_code == 200
    assert response.json()["status"] == "Contacted"

def test_delete_lead():
    response = client.delete("/leads/1")  # Assuming lead with ID 1 exists
    assert response.status_code == 200
    assert response.json()["message"] == "Lead deleted"
