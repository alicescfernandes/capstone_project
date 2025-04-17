# Django Final Project

A modern, responsive Django website with multiple pages and clean design.

## Requirements

You must have installed a Python version bigger than 3.9. For this project, the development was done under 3.12

You must have Node 22 installed on your machine

You must have a Docker runtime installed, you can either install Docker Desktop, Podman or Rancher and configure it to use the Docker CLI.

## Quick Start

1. Start the development environment
This will ensure that you get the correct dependencies installed and also Postgres and MongoDB running

```bash
docker-compose up --build
```

2. Visit <http://localhost:8000/> in your browser

## Documentation

- [Project Description](docs/DESCRIPTION.MD)

## Project Structure

```
final_project/
├── dashboard/           # Main Django project directory
├── docs/               # Project documentation
│   ├── DESCRIPTION.MD  # Project description
│   ├── USE_CASES_UML.md # Use cases and UML diagrams
│   └── SCENARIOS.md    # Project scenarios
├── venv/               # Python virtual environment
├── activate.sh         # Virtual environment setup script
└── .gitignore         # Git ignore rules
```

## Manual Commands

If you prefer to run commands manually:

1. Create and activate virtual environment:

```bash
python3 -m venv venv
source venv/Scripts/activate  # On Windows with Git Bash
```

2. Install dependencies:

```bash
pip3 install -r requirements.txt
```

3. Run migrations:

```bash
cd backend
python3 manage.py migrate
```

4. Start the development server:

```bash
python3 manage.py runserver
```

## Troubleshooting

1. If scripts are not executable:
   - Run `chmod +x *.sh` to make scripts executable

2. If Django is not found:
   - Make sure your virtual environment is activated
   - Run `pip3 install -r requirements.txt`

3. If migrations fail:
   - Run `python3 manage.py makemigrations`
   - Then `python3 manage.py migrate`

4. If templates aren't found:
   - Check that your app is in `INSTALLED_APPS`
   - Verify template directory structure
   - Ensure template names in views match actual files
