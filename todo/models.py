from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class DateTimeAbstract(models.Model):
    dt_create = models.DateTimeField(auto_now_add=True)
    dt_update = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Task(DateTimeAbstract):
    header = models.CharField(max_length=128)
    body = models.TextField()
    status = models.ForeignKey("todo.TaskStatus", on_delete=models.CASCADE, related_name="tasks")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="created_tasks")
    contributors = models.ManyToManyField(User, related_name="tasks")


class TaskStatus(DateTimeAbstract):
    name = models.CharField(max_length=32)


class TaskImage(DateTimeAbstract):
    image = models.ImageField()
