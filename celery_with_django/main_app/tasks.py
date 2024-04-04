from celery import shared_task
from time import sleep

@shared_task(bind=True)
def add(self,x:int,y:int) -> int:
    sleep(60)
    return x + y

@shared_task(bind=True)
def sub(self,x:int,y:int) -> int:
    sleep(120)
    return x - y