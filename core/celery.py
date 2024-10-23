# celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# create a Celery instance and configure it using the settings from Django
app = Celery('core')
app.conf.enable_utc = False
app.conf.update(timezone="Asia/Kolkata")
# load task modules from all registered Django app configs.
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'fetch-weather-every-5-minute': {
        'task': 'weather.tasks.fetch_weather_data',
        # 'schedule': crontab(minute=0, hour=0, day_of_week='*/2'),
        'schedule' : crontab(minute='*/2')
    },
    'generate-daily-summary': {
        'task': 'weather.tasks.calculate_daily_summary',
        'schedule': crontab(hour='23', minute='45'),  # Runs daily at 11:59 PM
    },
    'send-alert': {
        'task': 'alert.tasks.send_alert',
        'schedule': crontab(minute="*/5"),  # Runs daily at 11:59 PM
    },
}
# autodiscover tasks in all installed apps
app.autodiscover_tasks()



@app.task(bind=True)
def debug_task(self):
    print(f"Request {self.request!r}")
