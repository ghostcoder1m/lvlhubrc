import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_offer():
    response = client.post("/offers/", json={
        "name": "Special Offer",
        "description": "This is a special offer.",
        "discount_percentage": 20.0
    })
    assert response.status_code == 200
    assert response.json()["name"] == "Special Offer"

def test_read_offers():
    response = client.get("/offers/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_offer():
    response = client.get("/offers/1")  # Assuming offer with ID 1 exists
    assert response.status_code == 200
    assert "name" in response.json()

def test_update_offer():
    response = client.put("/offers/1", json={
        "description": "Updated offer description."
    })
    assert response.status_code == 200
    assert response.json()["description"] == "Updated offer description."

def test_delete_offer():
    response = client.delete("/offers/1")  # Assuming offer with ID 1 exists
    assert response.status_code == 200
    assert response.json()["message"] == "Offer deleted"
