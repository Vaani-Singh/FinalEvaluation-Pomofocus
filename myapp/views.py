from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def login_view(request):
    return render(request, 'login.html')

def signup_view(request):
    return render(request, 'signup.html')

def report_view(request):
    return render(request, 'report.html')

def settings_view(request):
    return render(request, 'settings.html')

