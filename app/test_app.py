import pytest
from app import app  # Ensure your main file is named app.py

@pytest.fixture
def client():
    """
    A pytest fixture that creates a temporary 'test client'.
    This allows us to send requests to the app without 
    manually running the server.
    """
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_endpoint(client):
    """
    Test the root endpoint (/) to ensure it returns 200 OK 
    and the correct greeting message.
    """
    # 1. Send a GET request to the root URL
    response = client.get('/')
    
    # 2. Check that the status code is 200 (Success)
    assert response.status_code == 200
    
    # 3. Check that the returned text matches exactly
    expected_text = "Hello, World! Your Python app is running."
    assert response.data.decode('utf-8') == expected_text
