#!/bin/bash

export SECRET_KEY="change_me"
export DEBUG=1
export DJANGO_ALLOWED_HOSTS="*"

export POSTGRES_ENGINE="django.db.backends.postgresql"
export POSTGRES_DB="django_db"
export POSTGRES_USER="django_user"
export POSTGRES_PASSWORD="djangopassword"
export POSTGRES_HOST="localhost"
export POSTGRES_PORT=5432

export REDIS_HOST="localhost"
export REDIS_PORT=6379
