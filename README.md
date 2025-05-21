Hiring Platform using Django and Python
This project is a web-based hiring platform built with Django, designed to connect job seekers with employers. It provides functionalities for users to register, create profiles, post job listings, apply for jobs, and manage applications.

Table of Contents
Features

Technologies Used

Project Structure & Modules

users

companies

jobs

applications

Technical Explanation

How to Use

Setup and Running the Application

Prerequisites

Cloning the Repository

Setting up the Virtual Environment

Installing Dependencies

Database Migrations

Creating a Superuser

Running the Development Server

Running Tests

Contributing

License

Features
User Authentication: Secure registration, login, and logout for both job seekers and employers.

User Profiles: Separate profiles for candidates (skills, experience, resume) and employers (company details).

Job Posting: Employers can create, edit, and manage job listings.

Job Search & Filtering: Candidates can search for jobs based on keywords, location, and other criteria.

Job Application: Candidates can apply for jobs directly through the platform.

Application Management: Employers can view and manage applications for their job postings.

Admin Panel: Django's built-in admin interface for managing users, jobs, and other data.

Technologies Used
Backend: Python 3.x, Django 4.x

Database: SQLite (default for development, configurable for production)

Frontend: HTML, CSS, JavaScript (standard Django templates)

Dependency Management: pip

Project Structure & Modules
The project is organized into several Django applications (modules), each responsible for a specific set of functionalities.

.
├── manage.py
├── requirements.txt
├── README.md
├── hiring_platform/           # Main Django project directory
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── users/                     # Handles user authentication and profiles
│   ├── migrations/
│   ├── templates/users/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── companies/                 # Manages company profiles
│   ├── migrations/
│   ├── templates/companies/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── jobs/                      # Manages job postings and search
│   ├── migrations/
│   ├── templates/jobs/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── applications/              # Handles job applications
│   ├── migrations/
│   ├── templates/applications/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
└── static/                    # Static files (CSS, JS, images)

users Module
What it is: This module is responsible for all user-related functionalities, including authentication and managing user profiles.

What it does:

Allows new users to register as either job seekers or employers.

Enables existing users to log in and log out.

Manages user profiles, allowing users to update their personal information, contact details, and for candidates, their resume/CV and skills.

Technical Explanation:

models.py: Defines the User model (often extended from Django's AbstractUser or a custom User model) and potentially CandidateProfile and EmployerProfile models with one-to-one relationships to the User model. These models store user-specific data.

views.py: Contains view functions/classes for user registration (register_candidate, register_employer), login (login_view), logout (logout_view), and profile management (profile_view, edit_profile).

forms.py: Defines Django forms for user registration and profile editing, handling data validation and saving.

urls.py: Maps URLs to the respective view functions (e.g., /register/, /login/, /profile/).

companies Module
What it is: This module manages information related to companies that post jobs on the platform.

What it does:

Allows employers to create and manage their company profiles, including company name, description, website, and location.

Associates job postings with specific company profiles.

Technical Explanation:

models.py: Defines the Company model, which stores details about each company. It might have a ForeignKey relationship to the EmployerProfile in the users app, linking a company to its managing employer.

views.py: Contains views for creating a new company profile (create_company), viewing a company's details (company_detail), and editing an existing company profile (edit_company).

forms.py: Provides forms for creating and updating Company instances.

urls.py: Defines URL patterns for company-related pages (e.g., /companies/create/, /companies/<int:pk>/).

jobs Module
What it is: This module is the core of the job board, handling the creation, display, and search of job listings.

What it does:

Allows employers to post new job openings with details like title, description, requirements, location, and salary range.

Enables job seekers to browse, search, and filter available job postings.

Displays detailed information for each job.

Technical Explanation:

models.py: Defines the Job model, which includes fields for job title, description, requirements, location, salary, posted date, and a ForeignKey to the Company model.

views.py: Implements views for listing all jobs (job_list), viewing a single job's details (job_detail), creating a new job posting (create_job), and editing existing jobs (edit_job). Search and filter logic would also reside here.

forms.py: Contains forms for creating and updating Job instances.

urls.py: Maps URLs for job listings (e.g., /jobs/, /jobs/<int:pk>/, /jobs/post/).

applications Module
What it is: This module manages the process of applying for jobs and tracking applications.

What it does:

Allows job seekers to submit applications for specific job postings.

Records application details, including the applicant, the job, and the application date.

Enables employers to view all applications for their posted jobs.

Technical Explanation:

models.py: Defines the Application model, which has ForeignKey relationships to both the Job model and the CandidateProfile (or User) model. It might also include fields for application status (e.g., "Pending", "Reviewed", "Rejected") and a timestamp.

views.py: Contains views for submitting an application (apply_for_job) and for employers to view applications for their jobs (employer_applications).

forms.py: Provides a simple form for submitting an application (often just a confirmation or additional message).

urls.py: Defines URLs for application submission (e.g., /jobs/<int:job_id>/apply/) and viewing applications (e.g., /applications/).

Technical Explanation
The project leverages Django's Model-View-Template (MVT) architectural pattern.

Models: Defined in models.py within each app, these are Python classes that represent database tables and define the structure of the data. Django's ORM (Object-Relational Mapper) allows interaction with the database using Python objects instead of raw SQL.

Views: Located in views.py, these are Python functions or classes that handle incoming HTTP requests, interact with models to fetch or save data, and then render an appropriate HTML template or return an HTTP response.

Templates: Stored in the templates/ directory of each app, these are HTML files with Django's templating language, allowing dynamic content to be inserted into the HTML.

URLs: Defined in urls.py files (both at the project level and within each app), these map URL patterns to specific view functions, routing incoming requests to the correct handler.

Forms: Defined in forms.py, these simplify data validation and rendering of HTML forms, making it easier to handle user input securely.

The overall flow typically involves: a user making a request (e.g., navigating to /jobs/), the URL dispatcher (urls.py) routing it to a view function (jobs.views.job_list), the view function querying the database via models (jobs.models.Job.objects.all()), and finally, the view rendering an HTML template (jobs/job_list.html) with the retrieved data.

How to Use
Register:

Navigate to the registration page (/register/).

Choose whether to register as a "Job Seeker" or an "Employer."

Fill in the required details and create your account.

Job Seekers:

Explore Jobs: Browse the list of available jobs on the homepage or /jobs/.

Search & Filter: Use the search bar and filters to find specific jobs.

View Job Details: Click on a job title to see its full description, requirements, and company details.

Apply for Jobs: On the job detail page, click the "Apply Now" button to submit your application.

Manage Profile: Update your candidate profile with your skills, experience, and upload your resume.

Employers:

Create Company Profile: After logging in, create your company's profile if you haven't already.

Post a Job: Navigate to the "Post Job" section (/jobs/post/) to create a new job listing, providing all relevant details.

Manage Jobs: View and edit your posted jobs.

View Applications: Access the applications submitted for your jobs to review candidates.

Admin Users:

Access the Django admin panel (/admin/) with superuser credentials.

Manage all users, jobs, companies, and applications directly.

Setup and Running the Application
Follow these steps to get the project up and running on your local machine.

Prerequisites
Python 3.8+

pip (Python package installer)

Cloning the Repository
First, clone the project repository to your local machine:

git clone https://github.com/ankitojha17/Hiring-platform-using-Django-and-python.git
cd Hiring-platform-using-Django-and-python

Setting up the Virtual Environment
It's highly recommended to use a virtual environment to manage project dependencies.

python -m venv venv

Activate the virtual environment:

On Windows:

.\venv\Scripts\activate

On macOS/Linux:

source venv/bin/activate

Installing Dependencies
Install all required Python packages using pip:

pip install -r requirements.txt

Database Migrations
Apply the database migrations to create the necessary tables in your database:

python manage.py makemigrations
python manage.py migrate

Creating a Superuser
Create a superuser account to access the Django admin panel:

python manage.py createsuperuser

Follow the prompts to set up a username, email, and password.

Running the Development Server
Start the Django development server:

python manage.py runserver

The application will now be accessible in your web browser at http://127.0.0.1:8000/.

Running Tests
To run the test cases for the project, ensure your virtual environment is active and run:

python manage.py test

This command will discover and run all tests defined in your Django apps.

Contributing
Contributions are welcome! If you'd like to contribute, please follow these steps:

Fork the repository.

Create a new branch (git checkout -b feature/your-feature-name).

Make your changes.

Write tests for your changes.

Ensure all tests pass.

Commit your changes (git commit -m 'Add new feature').

Push to the branch (git push origin feature/your-feature-name).

Open a Pull Request.

License
This project is licensed under the MIT License - see the LICENSE file for details. (If you have a specific license, replace MIT with your chosen license).
