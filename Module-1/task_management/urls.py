from django.contrib import admin
from django.urls import path,include
from task.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('task/',include("task.urls")),
]
