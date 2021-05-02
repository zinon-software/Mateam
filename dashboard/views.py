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
    

@login_required()
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
