# app.py
from flask import Flask, request, send_from_directory
import psycopg2

app = Flask(__name__)

# Function to connect to the database
def get_db_connection():
    conn = psycopg2.connect(
        host="ep-fragrant-rice-a4uz3q1a.us-east-1.aws.neon.tech",  # replace with your host
        database="test",  # replace with your database name
        user="test_owner",  # replace with your username
        password="BgY2ESmKnGU4",  # replace with your password
        sslmode="require"  # required by Neon
    )
    return conn

# Route to serve the HTML file directly
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# Route to handle form submission
@app.route('/', methods=['POST'])
def register_user():
    username = request.form['username']
    password = request.form['password']

    # Insert the data into the database
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
    conn.commit()
    cursor.close()
    conn.close()

    return f"User {username} registered successfully!"

if __name__ == '__main__':
    app.run(debug=True)
