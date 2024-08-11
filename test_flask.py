from app import app
import pytest

@pytest.fixture
def client():
    return app.test_client()

def test_hello(client):
    resp = client.get("/")
    assert resp.status_code == 200