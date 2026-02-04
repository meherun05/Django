from django.shortcuts import render
from django.http import HttpResponse
from task.forms import TaskForm,TaskModelForm
from task.models import Employess
from task.models import Task

# Create your views here.

def home(request):
    context = {
        "names" :["Meherun","Omri","Mehrab"]
    }
    return render(request,'index.html',context)

def managerDashboard(request):
    return render(request,'Dashboard/manager-Dashboard.html')

def userDashboard(request):
    return render(request,'Dashboard/user-Dashboard.html')

# def home(request):
#     return HttpResponse("Welcome to the Task mangement")

def createTask(request):
    # employees = Employess.objects.all()
    # form = TaskForm(employees = {"name":"John","id":1})
    # form = TaskForm(employees = employees)
    form = TaskModelForm() # only for get
    if request.method == "POST":
        # form = TaskForm(request.POST, employees = employees) # if use TaskForm
        form = TaskModelForm(request.POST)
        if form.is_valid():
            #  for model form data
            # print(form)
            form.save()
            return render(request,'taskForm.html',{"form":form,"message":"task added successfully"})
            # for Django Form data

            # data = form.cleaned_data
            # # print(form.cleaned_data)
            # title = data.get('title')
            # description = data.get('description')
            # dueDate = data.get('dueDate')
            # assignTo = data.get('assignTo')

            # task = Task.objects.create(title=title,description=description,dueDate=dueDate)
            
            # # assign employees to tasks
            # for empId in assignTo:
            #     employee = Employess.objects.get(id=empId)
            #     task.assignTo.add(employee)

            # return HttpResponse("Task Added Sucessfully")

    context = {"form": form}
    return render(request,'taskForm.html',context)

def view_task(request):
    tasks = Task.objects.all()
    return render(request,'showTask.html',{"tasks":tasks})
