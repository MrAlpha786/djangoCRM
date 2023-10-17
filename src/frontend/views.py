from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request, *args, **kwargs):
    # Check if user is logging in
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        # authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user=user)
            messages.success(request, "You have been logged in!")
        else:
            messages.error(request, "There was an error logging in. Please try again...")
        return redirect(home)

    return render(request, 'home.html', {})

def login_user(request, *args, **kwargs):
    pass

def logout_user(request, *args, **kwargs):
    pass
