from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from frontend.forms import AddRecordForm, SignUpForm
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


def customer_record(request, pk, *args, **kwargs):
    if request.user.is_authenticated:
        # Look up records
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record})

    messages.error(request, "You should be logged in to view that page...")
    return redirect(home)


def delete_record(request, pk, *args, **kwargs):
    if request.user.is_authenticated:
        Record.objects.get(id=pk).delete()
        messages.success(request, "Record deleted successfully.")
        return redirect(home)

    messages.error(request, "You must be logged in to do that...")
    return redirect(home)


def add_record(request, *args, **kwargs):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request, "Record added...")
                return redirect('home')
        return render(request, 'add_record.html', {'form': form})

    messages.success(request, "You must be logged in to do that...")
    return redirect(home)
