# Project Structure

This document outlines the structure of the Django project and explains the purpose of each component.

## Directory Structure

```
final_project/
├── app/                # Main app directory
│   ├── templates/     # HTML templates
│   │   └── app/      # App-specific templates
│   ├── views.py       # View functions
│   └── urls.py        # App URL configuration
├── manage.py          # Django management script
├── settings.py        # Project settings
├── urls.py           # Main URL configuration
├── asgi.py           # ASGI configuration
├── wsgi.py           # WSGI configuration
└── __init__.py       # Python package marker
```

## Key Components

### Core Project Files

- `manage.py`: Django's command-line utility for administrative tasks
- `settings.py`: Project settings and configuration
- `urls.py`: Main URL routing configuration
- `wsgi.py`: WSGI application entry point
- `asgi.py`: ASGI application entry point
- `__init__.py`: Marks the directory as a Python package

### Main App (`app/`)

The main application directory containing all the project's functionality:

- `templates/`: Contains all HTML templates
  - `app/`: App-specific templates
- `views.py`: Contains view functions that handle requests
- `urls.py`: App-specific URL routing

### Scripts

The `scripts/` directory contains shell scripts for common tasks:

- `activate.sh`: Activates the virtual environment
- `migrate.sh`: Runs database migrations
- `runserver.sh`: Starts the development server
- `createsuperuser.sh`: Creates a new superuser
- `newapp.sh`: Creates a new Django app

### Documentation

The `docs/` directory contains project documentation:

- `project_structure.md`: This file
- `creating_pages.md`: Guide for creating new pages
- `templates.md`: Template usage guide
- `commands.md`: Common Django commands
- `troubleshooting.md`: Troubleshooting guide 