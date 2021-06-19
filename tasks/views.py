from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django import forms
from django.urls import reverse_lazy

from .models import Task


User = get_user_model()


class TaskListView(ListView):

    model = Task

    def get_queryset(self):
        # original qs
        qs = super().get_queryset()
        # filter by assigned tasks and tasks assigned to you
        return qs.filter(Q(assigner=self.request.user) | Q(assignee=self.request.user))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Your tasks
        context['tasks_assigned_to_user'] = self.get_queryset().filter(
            assignee=self.request.user)
        # The tasks you've assigned
        context['assigned_tasks'] = self.get_queryset().filter(
            assigner=self.request.user)
        return context


class TaskDetailView(DetailView):

    model = Task


class TaskCreateView(CreateView):

    model = Task
    fields = ['name', 'priority_level', 'assigner', 'assignee', 'due_date',
              'description']


class TaskEditView(UpdateView):

    model = Task
    fields = ['name', 'priority_level', 'assigner', 'assignee', 'due_date',
              'description', 'completed']


class TaskDeleteView(DeleteView):

    model = Task
    success_url = reverse_lazy('')
