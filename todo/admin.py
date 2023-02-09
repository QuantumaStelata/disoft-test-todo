from django.contrib import admin

from . import models


admin.site.register(models.Task)
admin.site.register(models.TaskStatus)
admin.site.register(models.TaskImage)
admin.site.register(models.TaskComment)
