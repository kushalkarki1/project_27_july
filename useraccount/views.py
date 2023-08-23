from django.shortcuts import render, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from useraccount.forms import SignupForm, CustomLoginForm


def user_login(request):
    form = CustomLoginForm(request.POST or None)
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse("post:home"))
        else:
            errors = form.get_invalid_login_error()
            for error in errors:
                messages.add_message(request, messages.ERROR, error)
    context = {"form": form}
    return render(request, "login.html", context)


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("user:login"))


def signup(request):
    form = SignupForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("user:login"))
    context = {"form": form}
    return render(request, "signup.html", context)


