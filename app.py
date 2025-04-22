import os
import psycopg2
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    try:
        conn = psycopg2.connect(
            host=os.environ.get("DB_HOST"),
            port=os.environ.get("DB_PORT"),
            dbname=os.environ.get("DB_NAME"),
            user=os.environ.get("DB_USER"),
            password=os.environ.get("DB_PASSWORD"),
        )
        return "Connected to PostgreSQL successfully!"
    except Exception as e:
        return f"Database connection failed: {e}"
