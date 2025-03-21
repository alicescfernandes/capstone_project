# Project Structure

This document outlines the structure of the Django project and explains the purpose of each component.

## Directory Layout

```
final_project/
├── final_project/     # Main project directory
│   ├── settings.py   # Project settings
│   ├── urls.py       # Main URL configuration
│   └── wsgi.py       # WSGI configuration
├── pages/            # Pages app
│   ├── templates/    # HTML templates
│   ├── views.py      # View functions
│   └── urls.py       # App URL configuration
└── manage.py         # Django management script
```

## Key Files and Directories

### Main Project Directory (`final_project/`)
- `settings.py`: Contains all project settings, including:
  - Installed apps
  - Database configuration
  - Static files settings
  - Template settings
- `urls.py`: Main URL configuration file
- `wsgi.py`: WSGI application configuration

### Pages App (`pages/`)
- `views.py`: Contains view functions that handle requests
- `urls.py`: URL patterns for the pages app
- `templates/`: HTML templates organized by app name
  - `pages/`: Templates specific to the pages app

### Management Script (`manage.py`)
- Command-line utility for administrative tasks
- Used for running development server, migrations, etc.

## Template Organization

Templates are organized in a hierarchical structure:
```
templates/
└── pages/              # App-specific templates
    ├── home.html      # Home page template
    └── about.html     # About page template
```

This structure helps maintain separation of concerns and makes it easier to find and manage templates. 