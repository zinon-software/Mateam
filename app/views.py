from django.shortcuts import render, HttpResponse 

from django.utils import timezone
from django.http import JsonResponse
import json
import datetime

from .models import *
from .utils import cartData

# Create your views here.

def listProducts(request):
    products = Product.objects.all()
    data = cartData(request)
    cartItems = data['cartItems']
    return render(request, 'product.html', {"products":products, 'cartItems':cartItems})

def cart(request):
    data = cartData(request)
    context = {
        'items':data['items'],
        'order':data['order'],
        'cartItems':data['cartItems'],
    }    
    return render(request, "cart.html", context)

def checkout(request):
    data = cartData(request)
    context = {
        'items':data['items'],
        'order':data['order'],
        'cartItems':data['cartItems'],
    }
    return render(request, 'checkout.html', context)


def updateItem(request):
    productId = int(request.POST.get("productId"))
    action = request.POST.get("action")

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
    
    cart = cartData(request)
    cartItems = cart['cartItems']

    data = {
        "quantity": str(orderItem.quantity),
        "cartItems" : str(cartItems)
    }
    
    return JsonResponse(data, safe=False)

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    order.transaction_id = transaction_id    
    total = float(data['form']['total'])
    if total == order.get_cart_total:
        order.complete = True
    order.save()

    if order.shipping == True:
        ShippingAddress.objects.create(
            customer=customer,
            order = order,
            address= data['shipping']['address'],
            city= data['shipping']['city'],
            state= data['shipping']['state'],
            zipcode= data['shipping']['zipcode']
        )
    return JsonResponse('Payment submitted..', safe=False)




    
def tracking(request):
    customer = request.user.customer
    orders = Order.objects.filter(customer=customer)
    return render(request, 'tracking.html', {'orders':orders})









    