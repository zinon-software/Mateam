from django.shortcuts import render, redirect
from app.models import *

from django.http import JsonResponse
# Create your views here.


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
        print('الدالة no لا تقلع')
    
    return render(request, 'dashboard.html', context)

def update_order(request):
    orderId = request.POST.get('orderId')
    action = request.POST.get("action")
    try:
        order = Order.objects.get_or_create(id=orderId)
        order, created = Order.objects.get_or_create(id=orderId, complete=True)
        if action == 'add':
            order.status_order = 'BA'
        elif action == 'remove':
            order.status_order = 'FH'
        order.save()
    except:
        pass
    return JsonResponse(f'تمت الموافقة على الطلب رقم ..  {orderId}', safe=False)
    

def delivery(request):
    try:
        customer = request.user.customer
        if customer.status_customer == "AD" or customer.status_customer == "DL" :
            orders = Order.objects.all().order_by('-id')
            context = {"orders":orders}
        else:
            return redirect('listProducts')
    except:
        print('الدالة no لا تقلع')
    
    return render(request, 'delivery.html', context)

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
