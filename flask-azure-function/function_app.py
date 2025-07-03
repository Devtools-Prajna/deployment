import azure.functions as func
from flask import Flask, render_template, request
from datetime import datetime
import os

app = Flask(__name__)

# List to hold books (simulating a simple database)
books = []

@app.route('/')
def index():
    return render_template('index.html', books=books)

@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        date_added = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        books.append({'title': title, 'author': author, 'date_added': date_added})
        return redirect(url_for('index'))
    return render_template('add_book.html')

@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit_book(index):
    if request.method == 'POST':
        books[index]['title'] = request.form['title']
        books[index]['author'] = request.form['author']
        return redirect(url_for('index'))
    return render_template('update_book.html', book=books[index], index=index)

@app.route('/delete/<int:index>')
def delete_book(index):
    books.pop(index)
    return redirect(url_for('index'))

def main(req: func.HttpRequest) -> func.HttpResponse:
    """HTTP trigger for Azure Function."""
    with app.app_context():
        return func.WsgiMiddleware(app).handle(req)
