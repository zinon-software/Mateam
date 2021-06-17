from django.shortcuts import render, HttpResponse 

from django.contrib.auth.decorators import login_required

from django.utils import timezone
from django.http import JsonResponse
import json
import datetime

from .models import *
from .utils import cartData, guestOrder

# Create your views here.


def listProducts(request):
    products = Product.objects.all()
    data = cartData(request)
    cartItems = data['cartItems']
    context = {"products":products, 'cartItems':cartItems}
    return render(request, 'product.html', context)

def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'product_detail.html', {'product':product})



# @login_required()
def cart(request):
    data = cartData(request)
    context = {
        'items':data['items'],
        'order':data['order'],
        'cartItems':data['cartItems'],
    }    
    return render(request, "cart.html", context)

# @login_required()
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
    orderItem.price = product.price
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
    
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)

    else:
        customer, order = guestOrder(request, data)

    order.transaction_id = transaction_id    
    total = float(data['form']['total'])
    if total == order.get_cart_total:
        order.complete = True
        order.status_order = 'UR'
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




@login_required()
def tracking(request):
    customer = request.user.customer
    orders = Order.objects.filter(customer=customer).order_by('-id')
    return render(request, 'tracking.html', {'orders':orders})









    