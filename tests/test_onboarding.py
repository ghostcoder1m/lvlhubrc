import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_onboarding():
    response = client.post("/onboarding/", json={
        "user_id": 1,
        "status": "in_progress"
    })
    assert response.status_code == 200
    assert response.json()["status"] == "in_progress"

def test_read_onboardings():
    response = client.get("/onboarding/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_onboarding():
    response = client.get("/onboarding/1")  # Assuming onboarding with ID 1 exists
    assert response.status_code == 200
    assert "status" in response.json()

def test_update_onboarding():
    response = client.put("/onboarding/1", json={
        "status": "completed"
    })
    assert response.status_code == 200
    assert response.json()["status"] == "completed"

def test_delete_onboarding():
    response = client.delete("/onboarding/1")  # Assuming onboarding with ID 1 exists
    assert response.status_code == 200
    assert response.json()["message"] == "Onboarding deleted"
