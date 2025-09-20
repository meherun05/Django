from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'index.html')

def managerDashboard(request):
    return render(request,'Dashboard/manager-Dashboard.html')

def userDashboard(request):
    return render(request,'Dashboard/user-Dashboard.html')

# def home(request):
#     return HttpResponse("Welcome to the Task mangement")