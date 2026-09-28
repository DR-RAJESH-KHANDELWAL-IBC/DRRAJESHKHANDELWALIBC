from fastapi.testclient import TestClient

from backend.api.app import app

client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200


def test_metadata_endpoint():
    response = client.get("/metadata")
    assert response.status_code == 200
