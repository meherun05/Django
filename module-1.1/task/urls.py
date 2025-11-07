from django.contrib import admin
from django.urls import path
from task.views import managerDashboard,userDashboard,home,createTask

urlpatterns = [
    path('manager_dashboard/', managerDashboard),
    path('user_dashboard/', userDashboard),
    path('home/',home),
    path('createTask/',createTask)
]
