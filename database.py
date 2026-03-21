import sqlite3
import os
from werkzeug.security import generate_password_hash, check_password_hash

DB_PATH = "database.db"

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS favorites (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            gift_name TEXT NOT NULL,
            gift_json TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')
    conn.commit()
    conn.close()

def register_user(username, password):
    hashed_password = generate_password_hash(password)
    conn = get_db_connection()
    try:
        conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def login_user(username, password):
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
    conn.close()
    if user and check_password_hash(user['password'], password):
        return user
    return None

def add_favorite(user_id, gift_name, gift_data):
    conn = get_db_connection()
    # Check if already exists
    exists = conn.execute('SELECT id FROM favorites WHERE user_id = ? AND gift_name = ?', (user_id, gift_name)).fetchone()
    if not exists:
        conn.execute('INSERT INTO favorites (user_id, gift_name, gift_json) VALUES (?, ?, ?)', 
                     (user_id, gift_name, gift_data))
        conn.commit()
    conn.close()

def remove_favorite(user_id, gift_name):
    conn = get_db_connection()
    conn.execute('DELETE FROM favorites WHERE user_id = ? AND gift_name = ?', (user_id, gift_name))
    conn.commit()
    conn.close()

def get_favorites(user_id):
    conn = get_db_connection()
    favs = conn.execute('SELECT gift_json FROM favorites WHERE user_id = ?', (user_id,)).fetchall()
    conn.close()
    import json
    return [json.loads(f['gift_json']) for f in favs]

def is_favorite(user_id, gift_name):
    conn = get_db_connection()
    fav = conn.execute('SELECT id FROM favorites WHERE user_id = ? AND gift_name = ?', (user_id, gift_name)).fetchone()
    conn.close()
    return bool(fav)
