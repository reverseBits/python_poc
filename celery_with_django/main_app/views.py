from django.http import HttpResponse
from .tasks import add, sub
from send_mail_app.tasks import send_mail_func

def test(request):
    # In Celery, the .delay() method is used to enqueue a task for asynchronous execution.
    # When you define a Celery task using the @shared_task decorator,
    # you essentially create a task class with methods like .delay() to enqueue the task.
    result_add = add.delay(10, 20)
    result_sub = sub.delay(20,5)
    print("result of add , result of sub", result_add.status, result_sub.status)
    return HttpResponse("Queue add  and queue sub")

def send_mail_to_all(request):
    result= send_mail_func.delay()
    print("result of send mail : ", result.status)
    return HttpResponse("mail sent")