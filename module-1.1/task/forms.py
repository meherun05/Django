from django import forms
from task.models import Task,TaskDetails

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

class StyleFormMixin:
    """ Mixing to apply style to form field"""
    defaultClasses = "mt-2 border-2 border-gray-300 rounded-md shadow-sm focus:ring-2 focus:outline-none focus:border-transparent focus:ring-blue-500 w-full"
    defaultClassesDate = "mt-2 border-2 border-gray-300 rounded-md shadow-sm focus:ring-2 focus:outline-none focus:border-transparent focus:ring-blue-500 mx-2"
    defaultClassesCheckbox = "flex flex-wrap gap-4 mt-2"
    def applyStyledWidgets(self):
        for fieldName, field in self.fields.items():
            if isinstance(field.widget,forms.TextInput):
                field.widget.attrs.update({
                    'class': self.defaultClasses,
                    'placeholder': f"Enter {field.label.lower()}"
                })
            elif isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({
                    'class':self.defaultClasses,
                    'placeholder':f"Enter {field.label.lower()}",
                    'rows':5
                })
            elif isinstance(field.widget,forms.SelectDateWidget):
                field.widget.attrs.update({
                    'class': self.defaultClassesDate
                })
            elif isinstance(field.widget, forms.Select):
                field.widget.attrs.update({
                    'class': self.defaultClasses
                })
            elif isinstance(field.widget,forms.CheckboxSelectMultiple):
                field.widget.attrs.update({
                    'class':self.defaultClassesCheckbox
                })

# Django Model form
class TaskModelForm(StyleFormMixin,forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','description','dueDate','assignTo'] # the fields is just needed
        # exclude = ['project','isCompleted','isUpdated','createdAt','updateAt'] # the fields is not needed
        widgets = {
            'dueDate':forms.SelectDateWidget(),
            'assignTo':forms.SelectMultiple()
        }
        """ using mixin widgets"""

        ''' manual widgets'''
        # widgets = {
        #     'title': forms.TextInput(attrs={
        #         'class' : "mt-2 border-2 border-gray-300 rounded-md shadow-sm focus:ring-2 focus:outline-none focus:border-transparent focus:ring-blue-500 w-full",
        #         'placeholder':'Enter Title here..'
        #     }),
        #     'description':forms.Textarea(attrs={
        #         'class' : "mt-2 border-2 border-gray-300 rounded-md shadow-sm focus:ring-2 focus:outline-none focus:border-transparent focus:ring-blue-500 w-full",
        #         'placeholder':'describe the task..'
        #     }),
        #     'dueDate':forms.SelectDateWidget(attrs={
        #         'class' : "mt-2 border-2 border-gray-300 rounded-md shadow-sm focus:ring-2 focus:outline-none focus:border-transparent focus:ring-blue-500 mx-2",
        #     }),
        #     'assignTo':forms.CheckboxSelectMultiple(attrs={
        #         'class' : "",
        #         'placeholder':'Enter Title here..'
        #     })
        # }
    
    ''' widgets using mixins'''
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.applyStyledWidgets()

class TaskDetailsForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = TaskDetails
        fields = ['priority', 'notes']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.applyStyledWidgets()
