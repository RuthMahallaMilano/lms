import os

from celery import Celery

CELERY_RABBITMQ_ERLANG_COOKIE = os.getenv('CELERY_RABBITMQ_ERLANG_COOKIE')
CELERY_RABBITMQ_DEFAULT_USER = os.getenv('CELERY_RABBITMQ_DEFAULT_USER')
CELERY_RABBITMQ_DEFAULT_PASS = os.getenv('CELERY_RABBITMQ_DEFAULT_PASS')
CELERY_UTILS_VHOST = os.getenv('CELERY_UTILS_VHOST')
CELERY_RABBITMQ_HOST = os.getenv('CELERY_RABBITMQ_HOST')
CELERY_RABBITMQ_PORT = os.getenv('CELERY_RABBITMQ_PORT', 222)

public_broker_url = (f'amqp://{CELERY_RABBITMQ_DEFAULT_USER}:'
                     f'{CELERY_RABBITMQ_DEFAULT_PASS}@'
                     f'{CELERY_RABBITMQ_HOST}:{CELERY_RABBITMQ_PORT}/'
                     f'{CELERY_UTILS_VHOST}')
app = Celery('utils', broker=public_broker_url)

app.conf.update(
    task_serializer='json',
    accept_content=['json'],  # Ignore other content
    result_serializer='json',
    enable_utc=True,
    task_always_eager=bool(os.getenv('FLASK_DEBUG')),
)