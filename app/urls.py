from django.urls import path
from . import views
from . import api

urlpatterns = [
    
    path('', views.listProducts, name='listProducts'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('updateItem', views.updateItem, name='updateItem'),
    path('process_order', views.processOrder, name='process_order'),

    path('tracking', views.tracking, name='tracking'),

    ## api
    path('api/products', api.products_Api, name='products_Api'),
    path('api/product/<int:id>', api.product_detail_Api, name='product_detail_Api'),

    ## api class based view
    path('api/v2/products', api.ProductsApi.as_view(), name='ProductsApi'),
    path('api/v2/products/<int:id>', api.ProductDetailApi.as_view(), name='ProductDetailApi'),

]

