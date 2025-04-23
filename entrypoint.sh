#!/bin/sh

# Apply database migrations
python manage.py migrate
python manage.py makemigrations

# Create a superuser if it doesn't exist
echo "from django.contrib.auth.models import User; User.objects.filter(username='$DJANGO_SUPERUSER_USERNAME').exists() or User.objects.create_superuser('$DJANGO_SUPERUSER_USERNAME', '$DJANGO_SUPERUSER_EMAIL', '$DJANGO_SUPERUSER_PASSWORD')" | python manage.py shell

# Start the Gunicorn server
exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 0 flashcards.wsgi:application
