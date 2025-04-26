<<<<<<< HEAD
## 🚀 AI Safety Incident Log API

## 📆 Project Overview

A simple RESTful API built using *Python - Flask* as framework and *SQLite* as database to log and manage AI safety-related incidents.

---

## 💪 Technology Stack

- *Language*: Python 3
- *Framework*: Flask
- *ORM*: SQLAlchemy
- *Database*: SQLite

---

## 🛠 Setup Instructions

### 1. Clone the Repository (if using GitHub)

bash
git clone <your-repo-link>
cd your-repo-folder

(Or unzip the provided zip file if submitting without Git.)

---

### 2. Create and Activate Virtual Environment

bash
python -m venv venv
# Activate it:
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate


---

### 3. Install Dependencies

bash
pip install -r requirements.txt


Contents of requirements.txt:

Flask
Flask-SQLAlchemy


---

### 4. Set Up the Database

No manual database setup is needed!  
When you run the app, it will *automatically create* a incidents.db SQLite file with the required schema inside your project folder.

> However, if needed manually:
python
from app import app, db
with app.app_context():
    db.create_all()


---

### 5. Run the Flask App

bash
python app.py


The app will start on:

http://127.0.0.1:5000/


---

## ⚙ Database Configuration (Environment Variables)

For now, the database connection is hardcoded in app.py:
python
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///incidents.db'


(Optional) If you want, you can make it configurable via .env file using python-dotenv.

---

## 📢 API Endpoints and Examples

| Method | Endpoint             | Purpose                   | Example Command |
|:-------|:---------------------|:---------------------------|:----------------|
| GET    | /health             | Check server and database health | curl http://127.0.0.1:5000/health |
| GET    | /incidents          | List all incidents         | curl http://127.0.0.1:5000/incidents |
| GET    | /incidents/<id>     | Get incident by ID         | curl http://127.0.0.1:5000/incidents/1 |
| POST   | /incidents          | Create a new incident      | See POST example below |
| DELETE | /incidents/<id>     | Delete an incident by ID   | curl -X DELETE http://127.0.0.1:5000/incidents/1 |

---

### ➡ Example: Create New Incident (POST)

bash
curl -X POST http://127.0.0.1:5000/incidents \
-H "Content-Type: application/json" \
-d "{\"title\": \"AI Bot Failure\", \"description\": \"Bot gave biased responses\", \"severity\": \"High\"}"


---

## ✍ (Optional) Design Decisions and Challenges

- Implemented *centralized error handling* to ensure consistent JSON responses for errors.
- Used *application context management* to properly handle database operations outside route handlers.
- Decided to use *SQLite* for simplicity, but easily upgradable to *PostgreSQL* for production environments.
- Incorporated *input validation* for fields like title, description, and severity.
- Added a */health* endpoint to easily check API and database connectivity.

---

# ✅ Final Notes

- API is fully functional and REST-compliant.
- Minimal dependencies for easy local setup.
- Project is cleanly organized with professional error handling.

---