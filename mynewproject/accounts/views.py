from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the homepage!")
# Register View
def register_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        phone = request.POST['phone']
        bio = request.POST['bio']

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return redirect('register')

        user = CustomUser.objects.create_user(
            email=email,
            username=username,
            password=password,
            phone=phone,
            bio=bio
        )
        user.save()
        messages.success(request, 'Account created successfully!')
        return redirect('login')

    return render(request, 'accounts/register.html')


# Login View
def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')  # redirect to some dashboard
        else:
            messages.error(request, 'Invalid email or password')
            return redirect('login')

    return render(request, 'accounts/login.html')


# Logout View
def logout_view(request):
    logout(request)
    return redirect('login')
@login_required
def dashboard_view(request):
    return render(request, 'accounts/dashboard.html')