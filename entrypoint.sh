#!/bin/sh

until cd /code
do
    echo "Waiting for server volume..."
done


until python manage.py migrate
do
    echo "Waiting for db to be ready..."
    sleep 2
done


gunicorn --bind 0.0.0.0:7000 --workers 2 config.wsgi