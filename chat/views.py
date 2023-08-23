from django.shortcuts import render, get_object_or_404, reverse
from django.contrib.auth import get_user_model
from chat.models import Message
from django.db.models import Q
from chat.forms import MessageForm
from django.http import HttpResponseRedirect

User = get_user_model()

def message(request):
    users = User.objects.exclude(username=request.user.username)
    context = {"users": users, "user_list": True}
    return render(request, "chat.html", context)

def user_chat(request, username):
    user = get_object_or_404(User, username=username)
    users = User.objects.exclude(username=request.user.username)
    messages = Message.objects.filter(
                    Q(from_user=user, to_user=request.user) | Q(from_user=request.user , to_user=user)
                )
    form = MessageForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.from_user = request.user
        obj.to_user = user
        obj.save()
        return HttpResponseRedirect(reverse("chat:message", args=(username, )))
    context = {"users": users, "messages": messages, "form": form}
    return render(request, "chat.html", context)
