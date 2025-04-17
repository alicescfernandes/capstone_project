source venv/Scripts/activate
export $(grep -v '^#' ./infra/.env.dev | xargs)

cd backend
python manage.py makemigrations