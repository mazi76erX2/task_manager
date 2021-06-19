from django import forms

from .models import Task


class TaskCreateForm(forms.ModelForm):

    model = Task
    fields = ['name', 'priority_level', 'assigner', 'assignee', 'due_date',
              'description', 'completed']
    widgets = {
        'due_date': forms.DateTimeField()
    }
