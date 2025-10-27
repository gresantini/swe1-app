![GitHub Workflow Status (with event)](https://github.com/gresantini/swe1-app/actions/workflows/django.yml/badge.svg)
![License](https://img.shields.io/badge/license-MIT-yellow.svg)
![CI](https://img.shields.io/github/actions/workflow/status/gresantini/swe1-app/django.yml?label=CI%20Build&logo=github)
![Coverage](https://img.shields.io/badge/coverage-pending-yellow.svg)




# Django Polls App – CI Setup with GitHub Actions

## Overview
This project is a Django-based **Polls application** created as part of my assignment for setting up **Continuous Integration (CI)** with **GitHub Actions**.  
The application allows users to view polls, vote on them, and see the results.  
At this stage, the focus is on setting up automated testing and workflow integration, not deployment.

---

## Features
- Django web app with a simple polling system.
- Uses `python manage.py runserver` to run locally.
- Includes unit tests that can be executed with `python manage.py test`.
- Integrated with **GitHub Actions** to automatically test code on every push.

---
## Project Structure
```
swe1-app/
│
├── .ebextensions/ # Elastic Beanstalk configuration files
├── .github/
│ └── workflows/ # GitHub Actions workflow YAML files
│
├── mysite/ # Main Django project folder (settings, URLs, WSGI)
│
├── polls/ # Polls app folder
│ ├── pycache/
│ ├── migrations/ # Database migration files
│ ├── templates/
│ │ └── polls/ # HTML templates for polls app
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── tests.py
│ ├── urls.py
│ └── views.py
│
├── staticfiles/
│ └── admin/ # Admin static files collected by Django
│
├── .ebignore # Ignore rules for AWS Elastic Beanstalk
├── .gitignore # Ignore rules for Git
├── Procfile # Used by Elastic Beanstalk to run the app
├── README.md # This file
├── db.sqlite3 # SQLite database file
├── manage.py # Django’s command-line utility
└── requirements.txt # Project dependencies
```
## 🚀 Setup Instructions (Local)

Follow these steps to run the project locally:

1. **Clone this repository:**
   ```bash
   git clone https://github.com/gresantini/swe1-app
   cd swe1-app
2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt

6. **Run migrations:**
   ```bash
   python manage.py migrate

8. **Start the development server:**
   ```bash
   python manage.py runserver
   
10. **Access the app:**
    
   Open your browser and go to:
👉 http://127.0.0.1:8000/polls/




## Running tests
To run all tests (as configured in GitHub Actions):

python manage.py test

## Github Actions CI
This repository includes a GitHub Actions workflow that:

- Installs dependencies

- Runs Django tests automatically

- Ensures continuous integration before deployment

- The workflow file is located at: .github/workflows/django.yml



## Deployment (to be added)
Deployment to AWS Elastic Beanstalk is the next step in this project.
Once configured, this section will include:

EB environment setup instructions

Deployment command

URL to the live app


## Author

Name: Greta Santini

Course: CS 450 X: Software Engineering

Professor: Makendy Midouin

Date: October 2025
