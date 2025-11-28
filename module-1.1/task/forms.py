from django import forms

class TaskForm(forms.Form):
    title =  forms.CharField(max_length=255,label="Task Title")
    description = forms.CharField(widget=forms.Textarea, label="Task Description")
    dueDate = forms.DateField(widget=forms.SelectDateWidget,label="Due Date")
    assignTo = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=[],label="Assign To")

    def __init__(self,*args, **kwargs):
        # print(args,kwargs)
        employees = kwargs.pop("employees",[])
        # print (employees)
        super().__init__(*args,**kwargs)
        # print(self.fields)
        self.fields['assignTo'].choices = [(emp.id, emp.name) for emp in employees]
