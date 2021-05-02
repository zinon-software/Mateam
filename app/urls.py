from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.listProducts, name='listProducts'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('updateItem', views.updateItem, name='updateItem'),
    path('process_order', views.processOrder, name='process_order'),

    path('tracking', views.tracking, name='tracking'),
]

