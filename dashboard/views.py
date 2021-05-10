from django.shortcuts import render, redirect
from app.models import *

from django.contrib.auth.decorators import login_required

from django.http import JsonResponse
# Create your views here.

@login_required()
def dashboard(request):
    try:
        if request.user.is_authenticated:
            customer = request.user.customer
            if customer.status_customer == "AD":
                orders = Order.objects.all().order_by('-id')
                context = {"orders":orders}
            else:
                return redirect('listProducts')
        else:
            return redirect('listProducts')
    except:
        print('الدالة لا تقلع')
    
    return render(request, 'dashboard.html', context)

def order_details(request, pk):
    order = Order.objects.get(id=pk)
    items = order.orderitem_set.all()
    address = ShippingAddress.objects.get(order=order)
    cartItems = order.get_cart_items
    context = {
        'items':items,
        'address':address,
        'order':order,
        'cartItems':cartItems,
    }    
    return render(request, "order_details.html", context)
    
def update_order(request):
    orderId = request.POST.get('orderId')
    action = request.POST.get("action")
    try:
        order = Order.objects.get_or_create(id=orderId)
        order, created = Order.objects.get_or_create(id=orderId, complete=True)
        if action == 'add': # الموافقة على الطلب
            order.status_order = 'BA'
        elif action == 'remove': # الغاء الطلب
            order.status_order = 'FH'
        elif action == 'UP': # الشيف
            order.status_order = 'UP'
        elif action == 'BS': # سائق التوصيل
            order.status_order = 'BS'
        elif action == 'Booking':
            order.booking_driver = True
            order.driver = request.user.id
        elif action == 'DE': # تم التوصيل
            order.status_order = 'DE'
        order.save()
    except:
        pass
    return JsonResponse(f'تمت الموافقة على الطلب رقم ..  {orderId}', safe=False)

def statistics(request):
    Items = OrderItem.objects.all()
    the_sales = sum([item.get_total for item in Items])
    orders = Order.objects.all()
    
    context = {
        'the_sales': the_sales,
        'order': orders.count(),
        'UR': orders.filter(status_order='UR').count(),
        'BA': orders.filter(status_order='BA').count(),
        'UP': orders.filter(status_order='UP').count(),
        'BS': orders.filter(status_order='BS').count(),
        'DE': orders.filter(status_order='DE').count(),
        'FH': orders.filter(status_order='FH').count(),
        'NO': orders.filter(status_order='NO').count(),
    }
    return render(request, 'dashboard\statistics.html', context)



@login_required()
def delivery(request):
    try:
        customer = request.user.customer
        if customer.status_customer == "AD" or customer.status_customer == "DL" :
            orders = Order.objects.all().order_by('-id')
            context = {"orders":orders, "user":str(request.user.id),}
        else:
            return redirect('listProducts')
    except:
        print('الدالة no لا تقلع')
    
    return render(request, 'delivery.html', context)

@login_required()
def chef(request):
    try:
        customer = request.user.customer
        if customer.status_customer == "AD" or customer.status_customer == "SH" :
            orders = Order.objects.all().order_by('-id')
            context = {"orders":orders}
        else:
            return redirect('listProducts')
    except:
        print('الدالة no لا تقلع')
    
    return render(request, 'chef.html', context)
