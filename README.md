# Hillel REST API application

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

# Docker
docker-compose up -d 
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