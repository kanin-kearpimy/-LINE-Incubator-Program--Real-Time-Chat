from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_index():
    response = client.post('/api/add-list', json={'Test': 'test'})
    assert response.status_code == 200
    assert response.json() == {'Test': 'test'}