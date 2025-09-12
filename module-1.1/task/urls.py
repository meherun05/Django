from django.contrib import admin
from django.urls import path
from task.views import home

urlpatterns = [
    path('home/', home),
]
