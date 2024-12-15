from django.urls import path
from . import views

urlpatterns = [
    path('api/question', views.question, name='question'),
    path('api/messages/history', views.historial_messages, name='historial_messages'),
]