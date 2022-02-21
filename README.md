# Social Network REST API Application

# Setup

## Mandatory steps
1. Install Python3.9+
2. Install Pipenv

## Setup project
Install environment
```bash
# Create virtual environment
pipenv install

#pipenv install --dev
pipenv shell
```

Run django server
```bash
# Run migrations only on a project setup
python src/manage.py migrate

# Run server
python src/manage.py runserver
```

## Docker
```bash
# Run Postgres
docker-compose up -d postgres

# Run Rabbit-MQ
docker-compose up -d rabbit-mq
```

## Celery
```bash
# Start Celery
celery -A src.config worker -l INFO

# Start Celery beat
celery -A src.config beat -l INFO
```

## Formatting code
```bash
# Black
python -m black

# Flake8
flake8 .

# Isort
isort .