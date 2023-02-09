from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class DateTimeAbstract(models.Model):
    dt_create = models.DateTimeField(auto_now_add=True)
    dt_update = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AuthorAbstract(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="%(class)ss")

    class Meta:
        abstract = True


class Task(DateTimeAbstract, AuthorAbstract):
    header = models.CharField(max_length=128)
    body = models.TextField()
    status = models.ForeignKey("todo.TaskStatus", on_delete=models.CASCADE, related_name="tasks")
    contributors = models.ManyToManyField(User, blank=True, related_name="execute_tasks")

    def __str__(self):
        return self.header


class TaskStatus(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class TaskImage(DateTimeAbstract):
    task = models.ForeignKey("todo.Task", on_delete=models.CASCADE, related_name="images")
    image = models.ImageField()

    def __str__(self):
        return self.image.name


class TaskComment(DateTimeAbstract, AuthorAbstract):
    task = models.ForeignKey("todo.Task", on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()
    parent = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True, related_name="childs")

    def __str__(self):
        return self.text
