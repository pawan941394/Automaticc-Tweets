from celery import shared_task

import time

@shared_task()
def make_tweets():
    return