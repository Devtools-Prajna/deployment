import pytest
from flask_azure_function.app import app  # Corrected the import path

@pytest.fixture
def client():
    """Fixture to create a test client."""
    app.config['TESTING'] = True  # Set the app to testing mode
    with app.test_client() as client:
        yield client

def test_index(client):
    """Test if the index page loads successfully."""
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'Books' in rv.data  # Check if the term 'Books' appears in the page

def test_add_book(client):
    """Test the adding of a new book."""
    data = {
        'title': 'Test Book',
        'author': 'Test Author'
    }
    rv = client.post('/add', data=data, follow_redirects=True)
    assert rv.status_code == 200
    assert b'Test Book' in rv.data  # Ensure the new book appears in the page

def test_delete_book(client):
    """Test deleting a book from the list."""
    # Add a test book first
    data = {
        'title': 'Book to Delete',
        'author': 'Author'
    }
    client.post('/add', data=data, follow_redirects=True)
    
    # Get the index to find the book index
    rv = client.get('/')
    book_index = rv.data.decode().find('Book to Delete')

    # Delete the book
    rv = client.get(f'/delete/{book_index}', follow_redirects=True)
    assert rv.status_code == 200
    assert b'Book to Delete' not in rv.data  # Ensure the book is removed
