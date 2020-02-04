from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from user.forms import SignUpForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            messages.success(request, f"new account created: {username}")
            login(request, user)
            messages.info(request, f"you are now logged in as {username}")
            return redirect('main:homepage')
    else:
        form = SignUpForm()
    return render(request, 'user/register.html', {'form': form})


def logout_request(request):
    logout(request)
    messages.info(request, "logged out successfully!")
    return redirect("homepage")


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"you are now logged in as {username}")
                return redirect("homepage")
            else:
                messages.error(request, "invalid username or password")
        else:
            messages.error(request, "invalid username or password")
    form = AuthenticationForm()
    return render(request,
                  "user/login.html",
                  {"form": form})