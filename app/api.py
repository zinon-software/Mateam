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

class ProductsApi(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

class ProductDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    lookup_field = 'id'