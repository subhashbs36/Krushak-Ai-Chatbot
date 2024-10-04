# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('whatsapp-incoming/', views.whatsapp_incoming, name='whatsapp_incoming'),
]
