#!/bin/sh
# called by Dockerfile


cd /app

# start gunicorn
exec gunicorn --workers 2 --threads 2 --bind 0.0.0.0:8080 wsgi:app