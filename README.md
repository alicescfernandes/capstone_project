# Django Final Project

A modern, responsive Django website with multiple pages and clean design.

## Requirements

You must have installed a Python version bigger than 3.9. For this project, the development was done under 3.12

## Quick Start

1. Create and activate virtual environment:

```bash
./activate.sh
```

2. Start the development server:

```bash
./start.sh
```

3. Visit <http://localhost:8000/> in your browser

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
├── start.sh           # Development server startup script
├── requirements.txt    # Python dependencies
└── .gitignore         # Git ignore rules
```

## Available Scripts

- `activate.sh`: Creates and activates the virtual environment
- `start.sh`: Activates the virtual environment, runs migrations, and starts the development server

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
