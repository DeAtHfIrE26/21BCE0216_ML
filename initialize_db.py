# initialize_db.py
import sqlite3

def initialize_db():
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id TEXT PRIMARY KEY,
        request_count INTEGER
    )
    """)
    connection.commit()
    connection.close()

if __name__ == "__main__":
    initialize_db()
