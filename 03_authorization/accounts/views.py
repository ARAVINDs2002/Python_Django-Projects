from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages

def hero_page(request):
    if request.user.is_authenticated:
        return redirect('tasks:task_list')
    return render(request, 'accounts/hero.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Welcome {user.username}! Your account has been created.")
            return redirect('tasks:task_list')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/auth_form.html', {'form': form, 'title': 'Create Account', 'is_signup': True})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('tasks:task_list')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/auth_form.html', {'form': form, 'title': 'Welcome Back', 'is_signup': False})

def logout_view(request):
    logout(request)
    messages.info(request, "Logged out successfully.")
    return redirect('accounts:hero')
