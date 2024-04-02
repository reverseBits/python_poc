from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab
from time import sleep

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery_project.settings')

app = Celery('django_celery_project')

app.conf.enable_utc = False


# celery_send_events it use real time status of task in curses
app.conf.update(timezone = 'Asia/Kolkata',
                CELERY_SEND_EVENTS=True,)

app.config_from_object(settings, namespace="CELERY")

app.autodiscover_tasks()
