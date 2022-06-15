# Django Movies REST API Application 

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

## Run django server
```bash
# Run migrations only on a project setup
python src/manage.py migrate

# Run server
python src/manage.py runserver
```

## Formatting code
```bash
# Black
black .
