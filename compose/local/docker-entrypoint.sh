#!/bin/sh
echo "Starting server"

if [ "$POSTGRES_DB" = "hotel" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
      sleep 1
    done

    echo "PostgreSQL started"
fi


exec "$@"

python manage.py runserver 0.0.0.0:8000