from flask import Flask, request, send_from_directory
import psycopg2

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host="ep-fragrant-rice-a4uz3q1a.us-east-1.aws.neon.tech",
        database="test",
        user="test_owner",
        password="BgY2ESmKnGU4",
        sslmode="require"
    )
    return conn

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/', methods=['POST'])
def register_user():
    username = request.form['username']
    password = request.form['password']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
    conn.commit()
    cursor.close()
    conn.close()

    return f"User {username} registered successfully!"

# Vercel doesn't need app.run()
# if __name__ == '__main__':
#    app.run(debug=True)
