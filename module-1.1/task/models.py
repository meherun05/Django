from django.db import models

# Create your models here.

class Employess(models.Model):
    name = models.CharField(max_length=100);
    email = models.EmailField(unique=True);

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.TextField()
    start_date = models.DateField()
    desc = models.TextField(blank= True, null= True)

    def __str__(self):
        return self.name
    
class Task(models.Model):
    statusChoices = [
        ('PENDING','Pending'),
        ('IN_PROGRESS','In Progress'),
        ('COMPLETED','Completed'),
    ]
    project = models.ForeignKey(Project,on_delete=models.CASCADE,default=1)
    title = models.CharField(max_length= 250)
    description = models.TextField()
    dueDate = models.DateField()
    status = models.CharField(max_length=50, choices=statusChoices,default='PENDING')
    assignTo = models.ManyToManyField(Employess,related_name='employeeTask')
    isCompleted = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class TaskDetails(models.Model):
    HIGH = 'H'
    MEDIUM = 'M'
    LOW = 'L'
    PRIORITY_OPTION = (
        (HIGH, 'High'),
        (MEDIUM, 'Medium'),
        (LOW, 'Low'),
    )
    # stdId = models.CharField(max_length=255,primary_key= True)
    task = models.OneToOneField(Task, on_delete= models.CASCADE,related_name='details')
    # assingeTo = models.CharField(max_length=100)
    priority = models.CharField(max_length= 1,choices=PRIORITY_OPTION,default=LOW )
    notes = models.TextField(blank=True,null= True)

    def __str__(self):
        return f"Details form task {self.task.title}"

