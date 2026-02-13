from django.contrib import admin
from django.urls import path
from task.views import managerDashboard,userDashboard,home,createTask,view_task

urlpatterns = [
    path('manager_dashboard/', managerDashboard,name='manager_dashboard'),
    path('user_dashboard/', userDashboard),
    path('home/',home),
    path('createTask/',createTask),
    path('showTask/',view_task)
]
