import pytest
from app import app  # Import your Flask app

def test_homepage():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
