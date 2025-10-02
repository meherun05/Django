from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length= 250)
    description = models.TextField()
    dueDate = models.DateField()
    isCompleted = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

class TaskDetails(models.Model):
    HIGH = 'H'
    MEDIUM = 'M'
    LOW = 'L'
    PRIORITY_OPTION = (
        (HIGH, 'High'),
        (MEDIUM, 'Medium'),
        (LOW, 'Low'),
    )
    task = models.OneToOneField(Task, on_delete= models.CASCADE)
    assingeTo = models.CharField(max_length=100)
    priority = models.CharField(max_length= 1,choices=PRIORITY_OPTION,default=LOW )