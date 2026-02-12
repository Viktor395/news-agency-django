#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

mkdir -p staticfiles media articles_images news_images news_agency_django/news_images

python manage.py collectstatic --no-input
python manage.py migrate

python manage.py shell << END
from django.contrib.auth import get_user_model
User = get_user_model()
username = 'admin'
email = 'vel_v@ukr.net'
password = 'MaxPol777'

user, created = User.objects.get_or_create(username=username, defaults={'email': email})
user.set_password(password)
user.is_staff = True
user.is_superuser = True
user.save()
print(f"Superuser {username} updated/created successfully")
END
