# Django Final Project

A modern, responsive Django website with multiple pages and clean design.

## Quick Start

1. Create and activate virtual environment:
```bash
python -m venv venv
source venv/Scripts/activate  # On Windows with Git Bash
```

2. Install dependencies:
```bash
pip install django
```

3. Run migrations:
```bash
python manage.py migrate
```

4. Start the development server:
```bash
python manage.py runserver
```

5. Visit http://127.0.0.1:8000/ in your browser

## Documentation

- [Project Structure](docs/project_structure.md)
- [Creating New Pages](docs/creating_pages.md)
- [Template Guide](docs/templates.md)
- [Common Commands](docs/commands.md)
- [Troubleshooting](docs/troubleshooting.md)

## Getting Help

If you encounter any issues, please check the [Troubleshooting Guide](docs/troubleshooting.md) first. If you need additional help, feel free to open an issue.

## Project Structure

```
final_project/
├── app/                # Main app directory
│   ├── templates/     # HTML templates
│   ├── views.py       # View functions
│   └── urls.py        # App URL configuration
├── manage.py          # Django management script
├── settings.py        # Project settings
├── urls.py           # Main URL configuration
├── asgi.py           # ASGI configuration
├── wsgi.py           # WSGI configuration
└── __init__.py       # Python package marker
```

## Common Commands

- Run migrations:
```bash
python manage.py migrate
```

- Create a superuser:
```bash
python manage.py createsuperuser
```

- Start development server:
```bash
python manage.py runserver
```

- Create a new app:
```bash
python manage.py startapp app_name
```

## Troubleshooting

1. If Django is not found:
   - Make sure your virtual environment is activated
   - Run `pip install django`

2. If migrations fail:
   - Run `python manage.py makemigrations`
   - Then `python manage.py migrate`

3. If templates aren't found:
   - Check that your app is in `INSTALLED_APPS`
   - Verify template directory structure
   - Ensure template names in views match actual files