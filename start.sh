source venv/Scripts/activate
cd backend
# npm run build:css &
python manage.py makemigrations
python manage.py migrate
python manage.py runserver