import os

from celery import Celery
from datetime import timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'A.settings')
# hamnam bashe ba proj Celery('A')
celery_app = Celery('A')
# tasks.py haro pyda mikone
celery_app.autodiscover_tasks()

celery_app.conf.boroker_url = 'amqp://'
# barghasht natije
celery_app.conf.result_backend = 'rpc://'
# task haro be dade json tabdil mikone
celery_app.conf.task_serializer = 'json'
celery_app.conf.result_serializer = 'pickle'
# dade haye mojaz ke mitonan bian
celery_app.conf.accept_content = ['json', 'pickle']
# tarikh engheza task bara hazf shodan az saf
celery_app.result_expires = timedelta(days=1)
# bara task, client ro montazer bezaram? na
celery_app.conf.task_always_eager = False
# har worker 1 task ro hamzaman anjam midahad
# age tak ha sangine kam age sabok ziad mese 4
celery_app.conf.worker_prefetch_multiplier = 1
