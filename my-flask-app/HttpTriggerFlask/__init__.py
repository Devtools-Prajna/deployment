import azure.functions as func
from app import app  # Import Flask app from app.py
from azure.functions import WsgiMiddleware

main = WsgiMiddleware(app.wsgi_app).main
