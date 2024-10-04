from django.urls import path, include
#from .api import urls, views

from . import views

urlpatterns = [
    path('', views.chat_main, name='chat'),
    path('loan/', views.loan_form, name='loan_form'),
    path('<int:pk>/', views.chat, name='chat_id'),
    path('api/', include('chat.api.urls')),
]
