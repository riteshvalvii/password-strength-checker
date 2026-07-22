import sqlite3
from datetime import datetime


DATABASE_NAME = "password_history.db"


def create_database():

    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS password_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL,
            password_hash TEXT NOT NULL,
            date_used TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def get_password_history(user_id):

    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT password_hash
        FROM password_history
        WHERE user_id = ?
    """, (user_id,))

    passwords = cursor.fetchall()

    connection.close()

    return passwords


def save_password_hash(user_id, password_hash):

    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    date_used = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        INSERT INTO password_history
        (user_id, password_hash, date_used)
        VALUES (?, ?, ?)
    """, (
        user_id,
        password_hash.decode("utf-8"),
        date_used
    ))

    connection.commit()
    connection.close()