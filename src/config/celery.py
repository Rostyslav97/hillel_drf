from os import environ

from celery import Celery

environ.setdefault("DJANGO_SETTINGS_MODULE", "src.config.settings")

app = Celery("config")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()