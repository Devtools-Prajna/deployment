import pytest
from app import app  # Correct import for app.py in the root directory

def test_index():
    # Your test logic for the index route
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"Books" in response.data  # Check if the word "Books" exists in the page

def test_add_book():
    # Your test logic for adding a book
    client = app.test_client()
    response = client.post('/add', data={
        'title': 'The Catcher in the Rye',
        'author': 'J.D. Salinger'
    })
    assert response.status_code == 302  # Should redirect to the index page after adding
    assert b"The Catcher in the Rye" in response.data  # Verify the book was added

def test_edit_book():
    # Your test logic for editing a book
    client = app.test_client()
    client.post('/add', data={'title': '1984', 'author': 'George Orwell'})  # Adding a book first
    response = client.post('/edit/0', data={'title': '1984 (Updated)', 'author': 'George Orwell'})
    assert response.status_code == 302  # Should redirect to the index page after editing
    assert b"1984 (Updated)" in response.data  # Verify the updated book title

def test_delete_book():
    # Your test logic for deleting a book
    client = app.test_client()
    client.post('/add', data={'title': 'To Kill a Mockingbird', 'author': 'Harper Lee'})
    response = client.get('/delete/0')  # Delete the first book
    assert response.status_code == 302  # Should redirect to the index page after deletion
    assert b"To Kill a Mockingbird" not in response.data  # Verify the book is deleted
