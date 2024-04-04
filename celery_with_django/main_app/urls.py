from django.urls import path
from . import views

urlpatterns = [
    path('', views.test, name="test"),
    path('send_mail/', views.send_mail_to_all, name="sendmail"),
]