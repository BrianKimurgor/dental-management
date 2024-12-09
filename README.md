
---

# Dental Management System

This Django-based application manages dental clinics, doctors, patients, visits, and appointments. It leverages Django REST Framework for API development and provides a user-friendly interface for admin tasks.

---

## Table of Contents
1. [Project Setup](#project-setup)
   - [Prerequisites](#prerequisites)
   - [Clone the Repository](#clone-the-repository)
   - [Database Configuration](#database-configuration)
   - [Install Dependencies](#install-dependencies)
   - [Apply Migrations](#apply-migrations)
2. [Create a Superuser](#create-a-superuser)
3. [Running the Server](#running-the-server)
4. [API Documentation](#api-documentation)
5. [Features](#features)
6. [License](#license)

---

## Project Setup

### Prerequisites
- Python >= 3.10
- PostgreSQL (latest stable version)
- Git
- Virtual Environment (optional but recommended)

### Clone the Repository
Clone this repository:
```bash
git clone https://github.com/BrianKimurgor/dental-management.git
cd dental
```

### Install Dependencies
Set up a virtual environment and install the required packages:
```bash
python -m venv venv
source venv/bin/activate       # Linux/MacOS
venv\Scripts\activate          # Windows
pip install -r requirements.txt
```

### Database Configuration
Database settings are predefined in the `settings.py` file. The default configuration expects the following database credentials:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dental_management',
        'USER': 'dental_user',
        'PASSWORD': 'your_password',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```

To set up the database:

1. Open PostgreSQL and create the database:
   ```sql
   CREATE DATABASE dental_management;
   ```
2. Create a database user:
   ```sql
   CREATE USER dental_user WITH PASSWORD 'your_password';
   ```
3. Grant privileges to the user:
   ```sql
   GRANT ALL PRIVILEGES ON DATABASE dental_management TO dental_user;
   ```

If you need to customize the database credentials, edit the `DATABASES` section in `settings.py`.

---





### Apply Migrations
Run the following commands to set up the database schema:
```bash
python manage.py makemigrations
python manage.py migrate
```

---

## Create a Superuser
Create an admin user to access the Django admin interface:
```bash
python manage.py createsuperuser
```

---

## Running the Server
Run the Django development server:
```bash
python manage.py runserver
```
Visit the application at `http://127.0.0.1:8000/`.
Here there is a default route for you to log in, if yo have no account, you can register then login with the credentials you input to see the default route that leads you to clinics, where you can add clinics, on the on the nav bar, there are doctors and patients tab, you can navigate also and test by adding atient details and scheduling appointments.

---

## API Documentation
APIs are available at `http://127.0.0.1:8000/api/`. Here are some key endpoints:
- **Doctors**: `/api/doctors/`
- **Patients**: `/api/patients/`
- **Clinics**: `/api/clinics/`
- **Appointments**: `/api/appointments/`
- **Visits**: `/api/visits/`

The django rest framework well documents the APIs and is left open for testing

---

## Features
- **Authentication**: Secure login and logout using Django's authentication system.
- **Admin Interface**: Manage Clinics, Doctors, and Patients via Django Admin.
- **APIs**: CRUD functionality for Clinics, Doctors, Patients, Visits, and Appointments.
- **Responsive Design**: Basic navigation using Bootstrap.

---
## Study resources
These are the resources I used to help me build this project to completion:
```bash
https://www.w3schools.com/django/
https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p

```

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---