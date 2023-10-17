from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from frontend.forms import SignUpForm
from frontend.models import Record


def home(request, *args, **kwargs):
    # If user is just visiting the page
    if request.method == "GET":
        records = Record.objects.all()
        return render(request, 'home.html', {'records': records})

    username = request.POST['username']
    password = request.POST['password']
    # authenticate user
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user=user)
        messages.success(request, "You have been logged in!")
    else:
        messages.error(
            request, "There was an error logging in. Please try again...")
    return redirect(home)


def login_user(request, *args, **kwargs):
    pass


def logout_user(request, *args, **kwargs):
    logout(request)
    messages.info(request, "You have been logged out!")
    return redirect(home)


def register_user(request, *args, **kwargs):
    if request.method == "GET":
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
    
    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        # Authenticate and Login
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']

        user = authenticate(request, username=username, password=password)
        login(request, user)
        messages.success(request, "You have been successfully registered.")
        return redirect(home)
    
    return render(request, 'register.html', {'form': form})
    

