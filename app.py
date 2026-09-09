"""
app.py
------
Teacher Record Management System
Python + Streamlit + MySQL

Run with:
    streamlit run app.py
"""

import streamlit as st
import pandas as pd

from db import (
    add_teacher,
    get_teachers,
    search_teacher,
    update_teacher,
    delete_teacher,
)
from auth import check_login

st.set_page_config(
    page_title="Teacher Management System",
    page_icon="👨‍🏫",
    layout="wide",
)

DEPARTMENTS = [
    "Computer Science",
    "Mathematics",
    "Physics",
    "Chemistry",
    "English",
    "Management",
]

TABLE_COLUMNS = [
    "Teacher ID",
    "Name",
    "Email",
    "Phone",
    "Department",
    "Qualification",
    "Experience",
    "Salary",
]


# ---------------------------------------------------------
# Login Page
# ---------------------------------------------------------
def login_page():
    st.title("👨‍🏫 Teacher Record Management System")
    st.subheader("🔐 Admin Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if check_login(username, password):
            st.session_state["logged_in"] = True
            st.success("Login successful!")
            st.rerun()
        else:
            st.error("Invalid username or password")


# ---------------------------------------------------------
# Add Teacher
# ---------------------------------------------------------
def add_teacher_page():
    st.subheader("➕ Add Teacher")

    name = st.text_input("Teacher Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone")
    department = st.selectbox("Department", DEPARTMENTS)
    qualification = st.text_input("Qualification")
    experience = st.number_input("Experience (Years)", min_value=0, max_value=50, value=0)
    salary = st.number_input("Salary", min_value=0.0, value=0.0)

    if st.button("Add Teacher"):
        if name == "" or email == "":
            st.warning("Name and Email are required")
        else:
            try:
                add_teacher(name, email, phone, department, qualification, experience, salary)
                st.success("Teacher added successfully!")
            except Exception as e:
                st.error(f"Error: {e}")


# ---------------------------------------------------------
# View Teachers
# ---------------------------------------------------------
def view_teacher_page():
    st.subheader("📋 Teacher Records")
    dataframe = get_teachers()

    if dataframe.empty:
        st.info("No teacher records found.")
    else:
        st.dataframe(dataframe, use_container_width=True)


# ---------------------------------------------------------
# Search Teacher
# ---------------------------------------------------------
def search_teacher_page():
    st.subheader("🔍 Search Teacher")
    keyword = st.text_input("Enter name, email or department")

    if st.button("Search"):
        records = search_teacher(keyword)
        if records:
            dataframe = pd.DataFrame(records, columns=TABLE_COLUMNS)
            st.dataframe(dataframe, use_container_width=True)
        else:
            st.warning("No teacher found.")


# ---------------------------------------------------------
# Update Teacher
# ---------------------------------------------------------
def update_teacher_page():
    st.subheader("✏️ Update Teacher")

    teacher_id = st.number_input("Teacher ID", min_value=1, step=1)
    name = st.text_input("New Name")
    email = st.text_input("New Email")
    phone = st.text_input("New Phone")
    department = st.text_input("New Department")
    qualification = st.text_input("New Qualification")
    experience = st.number_input("New Experience", min_value=0)
    salary = st.number_input("New Salary", min_value=0.0)

    if st.button("Update Teacher"):
        try:
            update_teacher(teacher_id, name, email, phone, department, qualification, experience, salary)
            st.success("Teacher updated successfully!")
        except Exception as e:
            st.error(f"Error: {e}")


# ---------------------------------------------------------
# Delete Teacher
# ---------------------------------------------------------
def delete_teacher_page():
    st.subheader("🗑️ Delete Teacher")

    teacher_id = st.number_input("Enter Teacher ID", min_value=1, step=1)

    if st.button("Delete Teacher"):
        try:
            delete_teacher(teacher_id)
            st.success("Teacher deleted successfully!")
        except Exception as e:
            st.error(f"Error: {e}")


# ---------------------------------------------------------
# Dashboard (main layout after login)
# ---------------------------------------------------------
def dashboard():
    st.sidebar.title("📚 Teacher Management")
    option = st.sidebar.radio(
        "Menu",
        [
            "Dashboard",
            "Add Teacher",
            "View Teachers",
            "Search Teacher",
            "Update Teacher",
            "Delete Teacher",
        ],
    )

    if st.sidebar.button("Logout"):
        st.session_state["logged_in"] = False
        st.rerun()

    if option == "Dashboard":
        st.header("📊 Dashboard")
        dataframe = get_teachers()
        st.metric("Total Teachers", len(dataframe))
        if not dataframe.empty:
            st.subheader("Teacher Records")
            st.dataframe(dataframe, use_container_width=True)
    elif option == "Add Teacher":
        add_teacher_page()
    elif option == "View Teachers":
        view_teacher_page()
    elif option == "Search Teacher":
        search_teacher_page()
    elif option == "Update Teacher":
        update_teacher_page()
    elif option == "Delete Teacher":
        delete_teacher_page()


# ---------------------------------------------------------
# Main entry point
# ---------------------------------------------------------
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if st.session_state["logged_in"]:
    dashboard()
else:
    login_page()
