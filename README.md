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
---
## Setup Instructions

### 1. Extract and Open

- Extract the project files into a local directory.
- Open the project folder in **Visual Studio Code**.

### 2. Create a Virtual Environment

Open a new terminal inside VS Code and run:

```bash
virtualenv env
```

Activate the virtual environment:
```bash
.\env\Scripts\activate
```

*(For PowerShell users: you may need to run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` if you face activation issues.)*

### 3. Install Dependencies

Install all required libraries using:

```bash
pip install -r requirements.txt
```


### 4. Database Setup

- **No manual database setup needed!**
- Running the app will automatically create a SQLite database file named `triggers.db` with the required schema.

> Note: The database is **pre-populated** with some sample triggers coded inside `app.py`.

### 5. Run the Flask Application

```bash
python app.py
```

The app will start and be accessible at:

```
http://127.0.0.1:5000/
```

### 6. Database Configuration

The database is configured in `app.py` using SQLAlchemy URI:

```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///triggers.db'
```


---

## API Endpoints and Usage


### Using Postman

#### 1. Health Check (GET `/health`)
- **Method**: `GET`
- **URL**: `http://127.0.0.1:5000/health`
- **Body**: None
- **Expected Response**:
```json
{
  "Status": "Healthy"
}
```

#### 2. Get All Triggers (GET `/triggers`)
- **Method**: `GET`
- **URL**: `http://127.0.0.1:5000/triggers`
- **Body**: None
- **Expected Response**: List of all triggers

#### 3. Get Single Trigger (GET `/triggers/<id>`)
- **Method**: `GET`
- **URL**: `http://127.0.0.1:5000/triggers/1`
- **Body**: None
- **Expected Response**: Single trigger detail

#### 4. Create a New Trigger (POST `/triggers`)
- **Method**: `POST`
- **URL**: `http://127.0.0.1:5000/triggers`
- **Body**: 
  - Go to **Body** tab → **raw** → **JSON** format
  - Example:
```json
{
  "title": "Chatbot Confusion",
  "description": "Chatbot started giving wrong suggestions.",
  "severity": "Medium"
}
```
- **Expected Response**: "Trigger will be added to the database and displayed on screen for review"

#### 5. Delete a Trigger (DELETE `/triggers/<id>`)
- **Method**: `DELETE`
- **URL**: `http://127.0.0.1:5000/triggers/1`
- **Body**: None
- **Expected Response**: "Trigger will be deleted from the database"

---

### 2) Using terminal: 

| Method | Endpoint              | Purpose                         | Example in using browser                          | 
|:-------|:----------------------|:--------------------------------|:--------------------------------------------------|
| GET    | `/`                   | Test Route - Welcome Message    | Open in browser                                   |
| GET    | `/health`             | Health check for API and DB     | `curl http://127.0.0.1:5000/health`               |
| GET    | `/triggers`           | List all triggers               | `curl http://127.0.0.1:5000/triggers`             |
| GET    | `/triggers/<id>`      | Get specific trigger by ID      | `curl http://127.0.0.1:5000/triggers/1`           |
| POST   | `/triggers`           | Add a new trigger               | See POST example below                            |
| DELETE | `/triggers/<id>`      | Delete a trigger by ID          | `curl -X DELETE http://127.0.0.1:5000/triggers/1` |

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
