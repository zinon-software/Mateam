
from django.urls import path
from . import views

urlpatterns = [
    path('chat', views.get_chat, name='chat'),
    path('messages', views.get_messages, name='messages'),
    path('messages/<int:id>', views.get_messages_admin, name='messages_admin'),
]



