from django.shortcuts import render, redirect

def login_view(request):
    return render(request, 'login.html')

def home_view(request):
    return render(request, 'home.html')