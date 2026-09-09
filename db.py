"""
db.py
-------
All MySQL database logic for the Teacher Record Management System.
Keeping DB code separate from app.py makes the project easier to read,
test, and maintain.
"""

import os
import mysql.connector
import pandas as pd

# ---------------------------------------------------------
# Connection
# ---------------------------------------------------------
# Credentials are read from environment variables instead of being
# hardcoded, so you never commit real passwords to GitHub.
# Set these in a local .env file (see .env.example) or in your
# terminal/session before running the app.


def get_connection():
    """Create and return a new MySQL connection."""
    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""),
        database=os.getenv("DB_NAME", "teacher_db"),
    )
    return connection


# ---------------------------------------------------------
# Add Teacher
# ---------------------------------------------------------
def add_teacher(name, email, phone, department, qualification, experience, salary):
    connection = get_connection()
    cursor = connection.cursor()
    query = """
        INSERT INTO teachers
        (name, email, phone, department, qualification, experience, salary)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    values = (name, email, phone, department, qualification, experience, salary)
    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()


# ---------------------------------------------------------
# Get All Teachers
# ---------------------------------------------------------
def get_teachers():
    connection = get_connection()
    query = "SELECT * FROM teachers"
    dataframe = pd.read_sql(query, connection)
    connection.close()
    return dataframe


# ---------------------------------------------------------
# Search Teacher
# ---------------------------------------------------------
def search_teacher(keyword):
    connection = get_connection()
    cursor = connection.cursor()
    query = """
        SELECT * FROM teachers
        WHERE name LIKE %s
        OR email LIKE %s
        OR department LIKE %s
    """
    search_value = "%" + keyword + "%"
    cursor.execute(query, (search_value, search_value, search_value))
    records = cursor.fetchall()
    cursor.close()
    connection.close()
    return records


# ---------------------------------------------------------
# Update Teacher
# ---------------------------------------------------------
def update_teacher(teacher_id, name, email, phone, department, qualification, experience, salary):
    connection = get_connection()
    cursor = connection.cursor()
    query = """
        UPDATE teachers
        SET name=%s,
            email=%s,
            phone=%s,
            department=%s,
            qualification=%s,
            experience=%s,
            salary=%s
        WHERE teacher_id=%s
    """
    values = (name, email, phone, department, qualification, experience, salary, teacher_id)
    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()


# ---------------------------------------------------------
# Delete Teacher
# ---------------------------------------------------------
def delete_teacher(teacher_id):
    connection = get_connection()
    cursor = connection.cursor()
    query = "DELETE FROM teachers WHERE teacher_id=%s"
    cursor.execute(query, (teacher_id,))
    connection.commit()
    cursor.close()
    connection.close()
