from django.shortcuts import render
from django.http import HttpResponse
from task.forms import TaskForm,TaskModelForm
from django.utils import timezone
from task.models import Task, Employess
from django.db.models import Q,Count,Max,Min,Avg,Sum

# Create your views here.

def home(request):
    context = {
        "names" :["Meherun","Omri","Mehrab"]
    }
    return render(request,'index.html',context)

def managerDashboard(request):
    type = request.GET.get('type','all')
    print(type)
    now = timezone.now().date()
    all_tasks = Task.objects.select_related('details').prefetch_related('assignTo').all()
    today_tasks = Task.objects.select_related('details').prefetch_related('assignTo').filter(dueDate=now)

    # total_task = all_tasks.count()
    # pending_task = Task.objects.filter(status="PENDING").count()
    # inProgressTask = Task.objects.filter(status="IN_PROGRESS").count()
    # completeTask = Task.objects.filter(status="COMPLETED").count()

    counts = Task.objects.aggregate(
        total=Count('id'),
        inProgress=Count('id',filter=Q(status = 'IN_PROGRESS')),
        pendding=Count('id',filter=Q(status = 'PENDING')),
        completed=Count('id',filter=Q(status = 'COMPLETED'))
    )

    baseQuery = Task.objects.select_related('details').prefetch_related('assignTo')

    if type == 'COMPLETED':
        all_tasks = baseQuery.filter(status='COMPLETED')
        taskTitle = 'Completed Tasks'
    elif type == 'IN_PROGRESS':
        taskTitle = 'In Progress Tasks'
        all_tasks = baseQuery.filter(status='IN_PROGRESS')
    elif type == 'PENDING':
        taskTitle = 'Pending Tasks'
        all_tasks = baseQuery.filter(status='PENDING')
    else :
        taskTitle = 'All Tasks'
        all_tasks = baseQuery.all()

    context = {
        "tasks": all_tasks,
        "taskTitle" :  taskTitle,
        "today_tasks": today_tasks,
        "counts": counts,
        # "inProgressTask": inProgressTask,
        # "completeTask": completeTask,
        # "pending_task": pending_task
    }
    return render(request, 'Dashboard/manager-Dashboard.html', context)

def userDashboard(request):
    now = timezone.now().date()
    all_tasks = Task.objects.select_related('details').prefetch_related('assignTo').all()
    today_tasks = Task.objects.select_related('details').prefetch_related('assignTo').filter(dueDate=now)

    context = {
        "tasks": all_tasks,
        "today_tasks": today_tasks,
    }
    return render(request, 'Dashboard/user-Dashboard.html', context)

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

