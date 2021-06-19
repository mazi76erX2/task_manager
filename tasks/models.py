from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Task(models.Model):
    class PriorityChoices(models.IntegerChoices):
        P1 = 1
        P2 = 2
        P3 = 3

    name = models.CharField(max_length=64, null=False,
                            blank=False, unique=True)
    assigner = models.ForeignKey(User, on_delete=models.CASCADE,
                                 related_name="task_assigner")
    assignee = models.ForeignKey(User, on_delete=models.CASCADE,
                                 related_name="task_assignee")
    priority_level = models.PositiveSmallIntegerField(
        choices=PriorityChoices.choices, default=PriorityChoices.P1)
    due_date = models.DateTimeField(verbose_name="Due date")
    description = models.TextField(max_length=256, null=True, blank=True)
    completed = models.BooleanField()

    def __str__(self):
        return f'{self.name} - Assigned to: {self.assignee} - {self.due_date}'


class Response(models.Model):
    comment = models.CharField(max_length=256)
    commenter = models.OneToOneField(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    created_on = models.DateTimeField(
        verbose_name="Due date", auto_now_add=True)

    def __str__(self):
        return f'{self.commenter} - for task: {self.task.name}'
