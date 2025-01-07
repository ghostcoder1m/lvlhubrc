import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_campaign():
    response = client.post("/campaigns/", json={
        "name": "New Campaign",
        "description": "Campaign description",
        "user_id": 1
    })
    assert response.status_code == 200
    assert response.json()["name"] == "New Campaign"

def test_read_campaigns():
    response = client.get("/campaigns/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_campaign():
    response = client.get("/campaigns/1")  # Assuming campaign with ID 1 exists
    assert response.status_code == 200
    assert "name" in response.json()

def test_update_campaign():
    response = client.put("/campaigns/1", json={
        "description": "Updated description"
    })
    assert response.status_code == 200
    assert response.json()["description"] == "Updated description"

def test_delete_campaign():
    response = client.delete("/campaigns/1")  # Assuming campaign with ID 1 exists
    assert response.status_code == 200
    assert response.json()["message"] == "Campaign deleted"
