@echo off

rem Activate virtual environment
call D:\ReverseBits\Projects\django\celery_with_django\env\Scripts\activate.bat

rem Run Celery worker for add and sub queues
start cmd /k celery -A django_celery_project.celery worker -n worker_for_add_sub -Q add-queue,sub-queue -l INFO -P gevent

rem Run Celery worker for sendmail queue
start cmd /k celery -A django_celery_project.celery worker -n worker_for_send_mail -Q sendmail -l INFO -P gevent

rem Run Flower
start cmd /k celery --broker=redis://localhost:6379// flower