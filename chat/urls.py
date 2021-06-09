
from django.urls import path
from . import views

urlpatterns = [
    path('chat/<int:pk>/', views.chatroom, name='chatroom'),
    path('ajax/<int:pk>', views.ajax_load_messages, name='chatroom-ajax'),
    path('chatroom-admin', views.list_chat_for_admin, name='chatroom-admin'),
]



