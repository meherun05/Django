from django.shortcuts import render, redirect
from django.http import HttpResponse
from task.forms import TaskForm,TaskModelForm, TaskDetailsForm
from django.utils import timezone
from task.models import Task, Employess, TaskDetails
from django.db.models import Q,Count,Max,Min,Avg,Sum
from django.contrib import messages

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
    # form = TaskModelForm() # only for get
    task_form = TaskModelForm()
    details_form = TaskDetailsForm()

    if request.method == "POST":
        task_form = TaskModelForm(request.POST)
        details_form = TaskDetailsForm(request.POST)

        if task_form.is_valid() and details_form.is_valid():
            task = task_form.save()
            details = details_form.save(commit=False)
            details.task = task
            details.save()

            messages.success(request,"Task and details added successfully")
            return redirect('createTask')
            # return render(request, 'taskForm.html', {
            #     "task_form": task_form, 
            #     "details_form": details_form, 
            #     "message": "Task and details added successfully"
            # })

    context = {
        "task_form": task_form,
        "details_form": details_form
    }
    return render(request, 'taskForm.html', context)

def update_task(request, id):
    task = Task.objects.get(id=id)
    details, created = TaskDetails.objects.get_or_create(task=task)

    task_form = TaskModelForm(instance=task)
    details_form = TaskDetailsForm(instance=details)

    if request.method == "POST":
        task_form = TaskModelForm(request.POST, instance=task)
        details_form = TaskDetailsForm(request.POST, instance=details)

        if task_form.is_valid() and details_form.is_valid():
            task_form.save()
            details_form.save()
            messages.success(request, "Task updated successfully")
            return redirect('manager_dashboard')

    context = {
        "task_form": task_form,
        "details_form": details_form,
        "is_edit": True
    }
    return render(request, 'taskForm.html', context)

def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    messages.success(request, "Task deleted successfully")
    return redirect('manager_dashboard')

def view_task(request):
    tasks = Task.objects.all()
    return render(request,'showTask.html',{"tasks":tasks})
