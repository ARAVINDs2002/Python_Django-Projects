# Django Task Manager (CRUD with ModelForms)

A simple, clean Task Manager web application built with Django, demonstrating the core CRUD (Create, Read, Update, Delete) flow using Django's powerful `ModelForms`.

## How to Run This

### 1. Prerequisites
- Python 3.8+
- Django 4.0+

### 2. Setup and Installation
Navigate to the project directory:
```bash
cd taskmanager_project
```

Install dependencies (if not already installed):
```bash
pip install django
```

### 3. Database Setup
Run migrations to create the database schema:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Run the Server
Start the development server:
```bash
python manage.py runserver
```

Open your browser and navigate to `http://127.0.0.1:8000/`.

## Concepts Covered

- **Django Models**: Defining the data structure for tasks (Title, Description, Status).
- **ModelForms**: Automatically generating HTML forms from the `Task` model, handling both data display and validation.
- **Function-Based Views (FBVs)**: Implementing logic for listing, creating, updating, and deleting tasks.
- **URL Routing**: Mapping URLs to specific view functions.
- **Template Inheritance**: Using a `base.html` to share common layout elements across different pages.
- **Bootstrap 5 Styling**: Integrating a modern CSS framework for a responsive and clean UI.
- **CSRF Protection**: Using Django's built-in security for form submissions.

## What I Learned

1. **Efficiency of ModelForms**: Instead of manually creating form fields and handling validation logic, `ModelForms` allow us to link a form directly to a model, significantly reducing boilerplate code.
2. **Context Passing**: How views pass data (like task lists or form instances) to templates using dictionaries.
3. **ORM Operations**: Using `Task.objects.all()`, `.save()`, and `.delete()` to interact with the database without writing SQL.
4. **The CRUD Lifecycle**: Understanding how data flows from a user's browser (POST request) to the view, through the form/model, and into the database.
5. **Dynamic Routing**: Using `<int:pk>` in URLs to identify specific database records for updates and deletions.
