## AI Safety Trigger Log API

## Project Overview

A simple RESTful API built using **Python (Flask)** and **SQLite** to log and manage AI triggers or incidents in a safe and structured way.

---

## Technology Stack

- **Language**: Python 3
- **Framework**: Flask
- **ORM**: SQLAlchemy
- **Database**: SQLite

---
**Github link**: https://github.com/Kosalendra-Kalluri/sparklehood
## Setup Instructions

1) Extract the files into the local drive and open them in vscode
2) open a new terminal in vscode and create a virtual environment for you to work on
   ----> virtualenv env
   ----> .\env\Scripts\activate\ps1 - this will create a virtual environment
3) install all the dependencies using the requirements file
   ----> pip install -r requirements.txt
4) No manual setup of the database is needed, by running the app.py file it will automatically creates a 'trigger.db' SQLite database with a proper schema.
5) To mention the database is pre-populated I have included that part in the code, you can check out!!
6) Run the Flask app
   ----> python app.py
   This will start the app at:
   ----> http://127.0.0.1:5000/
7) Database is configured using the sqlalchemy database uri - sqlite:///triggers.db

---

## API Endpoints and Usage

| Method | Endpoint              | Purpose                         | Example in using browser                          | Example using postman
|:-------|:----------------------|:--------------------------------|:--------------------------------------------------|-----------------------
| GET    | `/`                   | Test Route - Welcome Message    | Open in browser                                   |Open in browser
| GET    | `/health`             | Health check for API and DB     | `curl http://127.0.0.1:5000/health`               |
| GET    | `/triggers`           | List all triggers/incidents     | `curl http://127.0.0.1:5000/triggers`             |
| GET    | `/triggers/<id>`      | Get specific trigger by ID      | `curl http://127.0.0.1:5000/triggers/1`           |
| POST   | `/triggers`           | Add a new trigger/incident      | See POST example below |
| DELETE | `/triggers/<id>`      | Delete a trigger/incident by ID | `curl -X DELETE http://127.0.0.1:5000/triggers/1` |

---

### Example: Create New Trigger (POST)

```bash
curl -X POST http://127.0.0.1:5000/triggers \
-H "Content-Type: application/json" \
-d "{\"title\": \"AI Model Crash\", \"description\": \"System failed under load\", \"severity\": \"High\"}"
```

---

## Design Decisions and Challenges

- Implemented **centralized error handling** for better API consistency.
- Used **application context management** correctly to initialize the database.
- Accepted **case-insensitive severity levels** (`Low`, `low`, etc.) for user-friendliness.
- Added a **health-check** endpoint for better system observability.
- Pre-populated the database with sample incidents for testing/demo purposes.

---

## Final Notes

- Fully functional RESTful API.
- Lightweight and beginner-friendly project structure.
- Can be easily scaled up to use PostgreSQL or MySQL for production.

---

