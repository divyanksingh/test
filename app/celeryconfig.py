import tasks

from celery import Celery

class CeleryConfig(object):

    BROKER_URL = 'redis://localhost:6379/0'    

    CELERY_RESULT_BACKEND = 'redis'

celeryConfig=CeleryConfig()

celery1 = Celery('tasks')

celery1.config_from_object(celeryConfig)