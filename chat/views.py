from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from .forms import ChatForm


# Create your views here.

def get_chat(request):
    contacts = Contact.objects.all()
    context = {'contacts':contacts, }
    return render(request, 'chat.html', context)

def get_messages(request):
    created_by = request.user
    contact, created = Contact.objects.get_or_create(user=created_by)
    chats = contact.chat_set.all().order_by('-date_added')

    if request.method == 'POST':
        messages = request.POST.get('messages')
        super_user = User.objects.all().first()
        data = Chat(created_by=contact, super_user=super_user, messages=messages)
        data.save()
        return redirect('messages')
    context = {'chats':chats}
    return render(request, 'messages.html', context)

def get_messages_admin(request, id):
    contact = Contact.objects.get(id=id)
    chats = contact.chat_set.all().order_by('-date_added')

    if request.method == 'POST':
        messages = request.POST.get('messages')
        super_user = request.user
        data = Chat(created_by=contact, super_user=super_user, messages=messages, customer=False)
        data.save()
        return redirect('messages/' + str(id))
    context = {'chats':chats}
    return render(request, 'messages.html', context)
