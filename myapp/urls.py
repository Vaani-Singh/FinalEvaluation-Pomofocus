from django.urls import path
from . import views
from .views import journal_view

urlpatterns = [
    path('', views.home, name='home'),             # Home page
    path('login/', views.login_view, name='login'),         # Login page
    path('signup/', views.signup_view, name='signup'),      # Signup page
    path('report/', views.report_view, name='report'),      # Report page
    path('settings/', views.settings_view, name='settings'),# Settings page
    path('journal/', journal_view, name='journal'), 
    path('game/', views.game_view, name='game'),
    path('music/', views.music_view, name='music'),


    path('tasks/', views.task_list, name='task_list'),
]
