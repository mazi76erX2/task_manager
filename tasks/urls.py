from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import TaskListView, TaskDetailView, TaskCreateView


urlpatterns = [
    path('', login_required(TaskListView.as_view()), name='home'),
    path('task/<int:pk>/', login_required(
         TaskDetailView.as_view()), name='task-detail'),
    path('task/create/', login_required(
         TaskCreateView.as_view()), name='task-create'),
    path('task/update/<int:pk>/', login_required(
         TaskCreateView.as_view()), name='task-edit'),
    path('task/delete/<int:pk>/', login_required(
         TaskCreateView.as_view()), name='task-delete'),
]
