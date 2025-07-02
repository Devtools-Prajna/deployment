from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_PAGE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Flask Azure App</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">
<div class="container mt-5">
    <h2 class="mb-4">Hello from Azure Web App + GitHub Actions + Flask</h2>

    {% if message %}
        <div class="alert alert-success">{{ message }}</div>
    {% endif %}

    <form method="POST">
        <div class="mb-3">
            <label for="username" class="form-label">Enter your name:</label>
            <input type="text" class="form-control" id="username" name="username" placeholder="John Doe" required>
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
    </form>
</div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def home():
    message = ""
    if request.method == 'POST':
        username = request.form.get('username')
        message = f"Welcome, {username}! You successfully submitted the form."
    return render_template_string(HTML_PAGE, message=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
