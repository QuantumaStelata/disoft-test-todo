from django.urls import path, include

from rest_framework import routers

from . import views


app_name = "api"

router = routers.DefaultRouter()
router.register(r'tasks', views.TaskViewSet)
router.register(r'task-statuses', views.TaskStatusViewSet)
router.register(r'task-images', views.TaskImageViewSet)
router.register(r'task-comments', views.TaskCommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
