import sqlite3
import os

DB_NAME = "test_users.db"


def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_database():
    conn = get_connection()
    conn.execute(
        """CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            age INTEGER
        )"""
    )
    conn.commit()
    conn.close()


def create_user(name, email, age=None):
    conn = get_connection()
    try:
        cursor = conn.execute(
            "INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
            (name, email, age),
        )
        conn.commit()
        return cursor.lastrowid
    except sqlite3.IntegrityError:
        raise ValueError(f"User with email '{email}' already exists")
    finally:
        conn.close()


def get_user_by_id(user_id):
    conn = get_connection()
    row = conn.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
    conn.close()
    if row is None:
        return None
    return dict(row)


def get_user_by_email(email):
    conn = get_connection()
    row = conn.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
    conn.close()
    if row is None:
        return None
    return dict(row)


def get_all_users():
    conn = get_connection()
    rows = conn.execute("SELECT * FROM users").fetchall()
    conn.close()
    return [dict(row) for row in rows]


def update_user(user_id, name=None, email=None, age=None):
    fields = []
    values = []
    if name is not None:
        fields.append("name = ?")
        values.append(name)
    if email is not None:
        fields.append("email = ?")
        values.append(email)
    if age is not None:
        fields.append("age = ?")
        values.append(age)
    if not fields:
        return False
    values.append(user_id)
    conn = get_connection()
    cursor = conn.execute(
        f"UPDATE users SET {', '.join(fields)} WHERE id = ?", values
    )
    conn.commit()
    updated = cursor.rowcount > 0
    conn.close()
    return updated


def delete_user(user_id):
    conn = get_connection()
    cursor = conn.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    deleted = cursor.rowcount > 0
    conn.close()
    return deleted


def delete_all_users():
    conn = get_connection()
    conn.execute("DELETE FROM users")
    conn.commit()
    conn.close()


def drop_database():
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)
