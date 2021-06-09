from django.urls import path
from . import views
from . import api

urlpatterns = [
    
    path('', views.listProducts, name='listProducts'),
    path('product/detail/<int:id>', views.product_detail, name='product_detail'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),

    path('updateItem/', views.updateItem, name='updateItem'),
    path('process_order', views.processOrder, name='process_order'),

    path('tracking', views.tracking, name='tracking'),

    ## api
    # path('api/products', api.products_Api, name='products_Api'),
    # path('api/product/<int:id>', api.product_detail_Api, name='product_detail_Api'),

    ## api class based view
    path('api/v2/products', api.ProductsApi.as_view(), name='ProductsApi'),
    path('api/v2/products/<int:id>', api.ProductDetailApi.as_view(), name='ProductDetailApi'),

    path('api/Order', api.OrderApi.as_view(), name='OrderApi'),
    path('api/Order/<int:id>', api.OrderDetailApi.as_view(), name='OrderDetailApi'),

    path('api/OrderItem', api.OrderItemApi.as_view(), name='OrderItemApi'),
    path('api/OrderItem/<int:id>', api.OrderItemDetailApi.as_view(), name='OrderItemDetailApi'),

    path('api/ShippingAddress', api.ShippingAddressApi.as_view(), name='ShippingAddressApi'),
    path('api/ShippingAddress/<int:id>', api.ShippingAddressDetailApi.as_view(), name='ShippingAddressDetailApi'),

]

