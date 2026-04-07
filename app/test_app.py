import pytest
from app import app 

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    """Checks if the home endpoint returns 200 and the correct string."""
    response = client.get('/')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Hello, World! Your Python app is running."
