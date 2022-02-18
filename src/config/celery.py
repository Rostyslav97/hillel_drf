from os import environ
from celery import Celery

environ.setdefault("DJANGO_SETTINGS_MODULE", "src.config.settings")

app = Celery("config")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

@app.task
def health_check():
    print("Celery works fine!")

@app.task
def beat_check():
    print("Celery beat works fine!")

@app.task
def create_post():
    print("Post was created")