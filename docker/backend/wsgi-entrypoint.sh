#!/bin/bash

until cd /app/backend/
do
    echo "Waiting for server volume..."
done

gunicorn server:app --bind 0.0.0.0:8000 --workers 4 --threads 4