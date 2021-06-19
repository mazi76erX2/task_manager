from django.contrib import admin
from .models import Task, Response


@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    pass

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass
