import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert b"Home Page" in rv.data

def test_about(client):
    rv = client.get('/about')
    assert rv.status_code == 200
    assert b"About Page" in rv.data
