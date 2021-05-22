# rest framewoark
from .models import *
from .serializer import *
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import generics

# @api_view()
# def products_Api(request):
#     products = Product.objects.all()
#     data = ProductSerializers(products, many=True).data
#     return Response({"data": data})

# @api_view()
# def product_detail_Api(request, id):
#     product = Product.objects.get(id=id)
#     data = ProductSerializers(product).data
#     return Response({"data": data})

# producte
class ProductsApi(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

class ProductDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    lookup_field = 'id'

# order
class OrderApi(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers

class OrderDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers
    lookup_field = 'id'

# OrderItem
class OrderItemApi(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializers

class OrderItemDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializers
    lookup_field = 'id'

# ShippingAddress
class ShippingAddressApi(generics.ListCreateAPIView):
    queryset = ShippingAddress.objects.all()
    serializer_class = ShippingAddressSerializers

class ShippingAddressDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShippingAddress.objects.all()
    serializer_class = ShippingAddressSerializers
    lookup_field = 'id'