from django.contrib import admin
from django.urls import path
from task.views import managerDashboard,userDashboard,home,createTask,view_task,update_task,delete_task

urlpatterns = [
    path('manager_dashboard/', managerDashboard,name='manager_dashboard'),
    path('user_dashboard/', userDashboard,name='userDashboard'),
    path('home/',home),
    path('createTask/',createTask,name='createTask'),
    path('edit-task/<int:id>/', update_task, name='update_task'),
    path('delete-task/<int:id>/', delete_task, name='delete_task'),
    path('showTask/',view_task)
]
