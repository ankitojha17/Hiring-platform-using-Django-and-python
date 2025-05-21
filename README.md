# Hiring Platform (Jobforme) – Built with Django 🧑‍💼💼

An online job portal where HRs can post jobs and candidates can apply.
This Django-based app is structured into modular apps to separate concerns
such as user authentication, HR features, and candidate profiles.

## 🚀 How to Run the App Locally

### 1. Clone the repo and install dependencies:
```bash
git clone <your-repo-url>
cd Hiring-platform-using-Django-and-python-master
pip install -r requirements.txt  # You can create one using: pip freeze > requirements.txt


python manage.py makemigrations
python manage.py migrate
python manage.py runserver
