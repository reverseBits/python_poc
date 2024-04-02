from django.http import HttpResponse
from .tasks import add, sub
from send_mail_app.tasks import send_mail_func

def test(request):
    result_add = add.delay(10,20)
    result_sub = sub.delay(20,5)
    print("result of add , result of sub", result_add.status, result_sub.status)
    return HttpResponse("Queue add  and queue sub")

def send_mail_to_all(request):
    result= send_mail_func.delay()
    print("result of send mail : ", result.status)
    return HttpResponse("mail sent")