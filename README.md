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

## Local Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
