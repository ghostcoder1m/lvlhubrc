import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_workflow():
    response = client.post("/workflows/", json={
        "name": "Marketing Workflow",
        "description": "A workflow for marketing automation.",
        "user_id": 1
    })
    assert response.status_code == 200
    assert response.json()["name"] == "Marketing Workflow"

def test_read_workflows():
    response = client.get("/workflows/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_workflow():
    response = client.get("/workflows/1")  # Assuming workflow with ID 1 exists
    assert response.status_code == 200
    assert "name" in response.json()

def test_update_workflow():
    response = client.put("/workflows/1", json={
        "description": "Updated workflow description."
    })
    assert response.status_code == 200
    assert response.json()["description"] == "Updated workflow description."

def test_delete_workflow():
    response = client.delete("/workflows/1")  # Assuming workflow with ID 1 exists
    assert response.status_code == 200
    assert response.json()["message"] == "Workflow deleted"
