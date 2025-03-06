
#Django To-Do App Project
    This is a Django-based To-Do List application with user authentication and task management.
  
#Apps in the Project:
   Tasks App: Manages tasks (add, update, delete).
Users App: 
  Handles user registration and authentication.
Static & Template Files:
   Static Folder: Contains CSS files for styling.
Templates Folder:
    Stores HTML files for frontend pages.
Database & Migrations:
    Uses SQLite (default Django database) or MySQL/PostgreSQL if configured.
   Migrations must be applied to create database tables.
Admin Panel:
  Superuser can manage all tasks and users.
  User Authentication:
  Users can register, log in, and log out.
  Only logged-in users can manage tasks.
  Project Setup Steps in PowerShell:
  Start a Django project.
  Create apps (tasks and users).
  Register apps in settings.py.
  Run migrations and create a superuser.
  Configure static files and templates.
  Start the server and test the application.

# 1. Create Django Project
django-admin startproject todo_app
cd todo_app

# 2. Create Apps
python manage.py startapp tasks
python manage.py startapp users

# 3. Run Migrations
python manage.py makemigrations
python manage.py migrate

# 4. Create Superuser
python manage.py createsuperuser

# 5. Start Development Server
python manage.py runserver
