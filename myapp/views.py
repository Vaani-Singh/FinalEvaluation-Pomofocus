from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
import requests


def home(request):
    return render(request, 'index.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials, please try again.')
    
    return render(request, 'login.html')


def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, 'Account created successfully!')
            return redirect('login')

    return render(request, 'signup.html')


def report_view(request):
    return render(request, 'report.html')

def journal_view(request):
    return render(request, 'journal.html')

def game_view(request):
    return render(request, 'game.html')


def settings_view(request):
    return render(request, 'settings.html')



def task_view(request):
    return render(request, 'tasks.html')

    
def music_view(request):
    return render(request, 'music.html')  



def get_all_tasks(request):
    response = requests.get('http://127.0.0.1:5000/api/tasks')
    tasks = response.json()  # Flask API returns JSON
    return JsonResponse(tasks, safe=False)


def task_list(request):
    # Fetch tasks from Flask API
    response = requests.get("http://127.0.0.1:5000/api/tasks")
    
    if response.status_code == 200:
        tasks = response.json()  # Parse the JSON response
    else:
        tasks = []  # If the API fails, set an empty list
    
    return render(request, "tasks.html", {"tasks": tasks})


def add_task(request):
    if request.method == 'POST':
        task_title = request.POST.get('title')
        response = requests.post(
            'http://127.0.0.1:5000/api/tasks',
            json={"title": task_title}
        )
        if response.status_code == 201:
            return JsonResponse(response.json(), status=201)
        else:
            return JsonResponse({"error": "Failed to add task"}, status=400)
