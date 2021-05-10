
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('update_order', views.update_order, name='update_order'),
    path('delivery', views.delivery, name='delivery'),
    path('chef', views.chef, name='chef'),
    path('order_details/<int:pk>', views.order_details, name='order_details'),
    path('statistics', views.statistics, name="statistics"),
]



