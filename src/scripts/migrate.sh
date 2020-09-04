#! /bin/bash

. ./scripts/env.sh
source ../venv/bin/activate

# ./src/manage.py flush
./manage.py makemigrations
./manage.py migrate

echo 'Creating user admin'
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@myproject.com', 'password')" | python manage.py shell



