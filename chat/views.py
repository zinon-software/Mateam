from django.shortcuts import get_object_or_404, render


from .models import User, Message
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.db.models import Q
import json

# Create your views here.

@login_required
def chatroom(request, pk):
    # other_user = get_object_or_404(User, pK=pK)
    other_user = User.objects.get(id=pk)
    messages = Message.objects.filter(
        Q(receiver=request.user, sender=other_user)
    )
    messages.update(seen=True)
    messages = messages | Message.objects.filter(Q(receiver=other_user, sender=request.user))

    return render(request, "chatroom.html", {"other_user":other_user, "messages": messages})

@login_required
def ajax_load_messages(request, pk):
    # other_user = get_object_or_404(User, pK=pK)
    other_user = User.objects.get(id=pk)
    messages = Message.objects.filter(seen=False).filter(
        Q(receiver=request.user, sender=other_user)
    )
    message_list = [{
        "sender": message.sender.username,
        "message": message.message,
        "sent": message.sender == request.user
    } for message in messages]
    messages.update(seen=True)

    if request.method == "POST":
        message = json.loads(request.body)
        m = Message.objects.create(receiver=other_user, sender=request.user, message=message)
        message_list.append({
            "sender": request.user.username,
            "message": m.message,
            "sent": True,
        })

    return JsonResponse(message_list, safe=False)


def list_chat_for_admin(request):
    chatrooms =  Message.objects.filter(receiver=request.user, seen=False)
    coun = chatrooms.count()
    return render(request, "list_chat_for_admin.html", { "chatrooms": chatrooms, 'coun':coun})

