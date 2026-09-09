# 👨‍🏫 Teacher Record Management System

A simple **Teacher Record Management System** built with **Python, Streamlit, and MySQL**. It supports admin login and full CRUD (Create, Read, Update, Delete) operations on teacher records through a clean web dashboard.

## Features

- 🔐 Admin login (password stored as a SHA-256 hash)
- 📊 Dashboard with total teacher count and full record view
- ➕ Add Teacher
- 📋 View Teachers
- 🔍 Search Teacher (by name, email, or department)
- ✏️ Update Teacher
- 🗑️ Delete Teacher
- 🚪 Logout

## Architecture

```
                Streamlit Web App
                       |
        +--------------+--------------+
        |              |              |
      Login         Dashboard       Logout
                       |
             +---------+---------+
             |         |         |
            Add      Search    Manage
             |         |         |
             +---------+---------+
                       |
                    MySQL DB
                       |
                teacher_records
```

## Tech Stack

| Layer      | Technology              |
|------------|--------------------------|
| Frontend   | Streamlit                |
| Backend    | Python                   |
| Database   | MySQL                    |
| DB Driver  | mysql-connector-python   |
| Data       | pandas                   |

## Project Structure

```
teacher_management_system/
│
├── app.py               # Streamlit UI and page routing
├── db.py                # Database functions (add/get/search/update/delete)
├── auth.py               # Admin login logic
├── setup_database.sql   # Creates the database, tables, and default admin
├── requirements.txt      # Python dependencies
├── .env.example          # Template for environment variables
├── .gitignore
├── LICENSE
└── README.md
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/teacher-management-system.git
cd teacher-management-system
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up MySQL

Make sure MySQL is installed and running, then run the setup script:

```bash
mysql -u root -p < setup_database.sql
```

This creates the `teacher_db` database, the `teachers` and `admins` tables, and a default admin account.

### 5. Configure environment variables

Copy the example file and fill in your MySQL credentials:

```bash
cp .env.example .env
```

Then edit `.env`:

```
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=teacher_db
```

Load the variables before running the app, for example:

```bash
export $(cat .env | xargs)   # macOS/Linux
```

(On Windows, set them with `set VAR=value` or use a tool like `python-dotenv`.)

### 6. Run the application

```bash
streamlit run app.py
```

Streamlit will open the app at `http://localhost:8501`.

### 7. Log in

Use the default admin credentials created by `setup_database.sql`:

```
Username: admin
Password: admin123
```

> ⚠️ Change this password (or add a new admin) before using the app for anything real.

## Usage

- **Add Teacher** — fill in the form (name and email are required) and click **Add Teacher**.
- **View Teachers** — see all records in a sortable table.
- **Search Teacher** — search by name, email, or department.
- **Update Teacher** — enter the Teacher ID and new details, then click **Update Teacher**.
- **Delete Teacher** — enter the Teacher ID and click **Delete Teacher**.

## Notes on Security

This project stores admin passwords as SHA-256 hashes rather than plain text. For a real production deployment, consider:

- Using a salted hashing library such as `bcrypt` or `passlib`
- Enforcing HTTPS
- Adding role-based access control
- Using a managed/secrets-based configuration instead of `.env` files

## License

This project is licensed under the [MIT License](LICENSE).
