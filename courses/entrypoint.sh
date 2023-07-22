#!/bin/sh

if [ "$DB_USER" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $DB_HOST $DB_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py create_db
gunicorn --bind 0.0.0.0:3000 manage:app

exec "$@"