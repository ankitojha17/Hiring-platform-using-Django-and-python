

# Hiring Platform (Jobforme) – Built with Django 🧑‍💼💼

An online job portal where HRs can post jobs and candidates can apply. This Django-based app is modularized into different apps to separate user roles and responsibilities clearly.

---

## 🚀 How to Run the App Locally

### 1. Clone the repo and install dependencies:
```bash
git clone <your-repo-url>
cd Hiring-platform-using-Django-and-python-master
pip install -r requirements.txt  # You can create one using: pip freeze > requirements.txt

````

### 2. Run migrations and start the development server:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Visit the app in your browser at:
👉 `http://127.0.0.1:8000/`

---

## 🧩 Modules Overview

### 🔐 `authuser/`

* Handles login, registration, and role-based authentication
* Custom user model to support both HR and Candidate roles

### 🧑‍💼 `hr/`

* HR dashboard interface
* Post job listings
* Review and manage candidate applications

### 🧑‍💻 `candidate/`

* Candidate dashboard
* Browse and apply for jobs
* Upload profile and resumes

### ⚙️ `jobforme/`

* Core Django settings, routing, and configuration
* Central project management

---

## 🛠️ Technical Stack

* **Framework**: Django 3.x+
* **Database**: SQLite (for local development)
* **Authentication**: Django’s built-in auth with customization
* **Media Handling**: For profile uploads, etc.
* **Frontend**: Django templates + Bootstrap (or similar)

---

## 🧪 How to Run Tests

Run this command to execute test cases:

```bash
python manage.py test
```

---

## 📂 Folder Structure

```
├── authuser/      # User login/register logic
├── candidate/     # Candidate-specific features
├── hr/            # HR-related functionality
├── jobforme/      # Main project configuration
├── media/         # Uploaded files (e.g., resumes)
├── db.sqlite3     # Local database
├── manage.py      # Django entry point
```

---


