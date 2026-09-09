"""
auth.py
-------
Simple admin authentication against the `admins` table.

Passwords are stored as SHA-256 hashes rather than plain text.
This is a lightweight improvement over storing raw passwords -
for a real production system, use a dedicated library such as
`bcrypt` or `passlib` with salting.
"""

import os
import hashlib
import mysql.connector


def hash_password(password: str) -> str:
    """Return a SHA-256 hex digest of the given password."""
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""),
        database=os.getenv("DB_NAME", "teacher_db"),
    )


def check_login(username: str, password: str) -> bool:
    """Return True if username/password matches a row in `admins`."""
    connection = get_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM admins WHERE username=%s AND password=%s"
    cursor.execute(query, (username, hash_password(password)))
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    return result is not None
