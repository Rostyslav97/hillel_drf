# Hillel REST API applicstion

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
python manage.py migrate

# Run server
python manage.py runserver
```