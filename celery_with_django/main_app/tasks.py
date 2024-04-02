from celery import shared_task
from time import sleep

@shared_task(bind=True)
def add(self,x,y):
    sleep(60)
    return x + y

@shared_task(bind=True)
def sub(self,x,y):
    sleep(120)
    return x - y