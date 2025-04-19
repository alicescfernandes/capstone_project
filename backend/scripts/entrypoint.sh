#!/bin/sh

# Save this with the UNIX Line Endings (LF)

echo "Applying migrations..."
python manage.py makemigrations  --verbosity 3
python manage.py migrate

echo "Creating superuser (if not exists)..."
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='${DJANGO_SUPERUSER_USERNAME}').exists():
    User.objects.create_superuser(
        '${DJANGO_SUPERUSER_USERNAME}',
        '${DJANGO_SUPERUSER_EMAIL}',
        '${DJANGO_SUPERUSER_PASSWORD}'
    )
EOF

exec python manage.py runserver 0.0.0.0:8000


