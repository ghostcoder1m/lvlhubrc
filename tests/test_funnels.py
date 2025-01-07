import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_funnel():
    response = client.post("/funnels/", json={
        "name": "Sales Funnel",
        "description": "A funnel for sales.",
    })
    assert response.status_code == 200
    assert response.json()["name"] == "Sales Funnel"

def test_read_funnels():
    response = client.get("/funnels/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_funnel():
    response = client.get("/funnels/1")  # Assuming funnel with ID 1 exists
    assert response.status_code == 200
    assert "name" in response.json()

def test_update_funnel():
    response = client.put("/funnels/1", json={
        "description": "Updated funnel description."
    })
    assert response.status_code == 200
    assert response.json()["description"] == "Updated funnel description."

def test_delete_funnel():
    response = client.delete("/funnels/1")  # Assuming funnel with ID 1 exists
    assert response.status_code == 200
    assert response.json()["message"] == "Funnel deleted"
