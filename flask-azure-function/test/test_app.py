import pytest
from flask_azure_function.app import app  # Adjust the import path to reflect your folder structure

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index(client):
    # Test the index route to ensure it's working
    response = client.get('/')
    assert response.status_code == 200
    assert b"Books" in response.data  # Adjust based on the text on your homepage

def test_add_book(client):
    # Test the POST request for adding a new book
    response = client.post('/add', data={'title': 'Test Book', 'author': 'Test Author'})
    assert response.status_code == 302  # Redirects after POST request (302)
    assert b"Books" in response.data  # Check if it redirects to the main page (index)
    
def test_delete_book(client):
    # Test delete book route
    client.post('/add', data={'title': 'Test Book', 'author': 'Test Author'})
    response = client.get('/delete/0')  # Assuming the index is 0
    assert response.status_code == 302
    assert b"Books" in response.data  # After deletion, it should return to the index page

