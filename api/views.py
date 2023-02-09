from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend

from . import serializers
from todo import models


class TaskViewSet(ModelViewSet):
    serializer_class = serializers.TaskSerializer
    queryset = models.Task.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["status", "status__name"]
        
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        user_is_author = request.user == instance.author
        user_is_contributor = instance.contributors.filter(id=request.user.id).exists()

        if not user_is_author and not user_is_contributor:
            return Response({
                "error": "Forbidden"
            }, status=status.HTTP_403_FORBIDDEN)
        
        return super().destroy(request, *args, **kwargs)
        

class TaskStatusViewSet(ModelViewSet):
    serializer_class = serializers.TaskStatusSerializer
    queryset = models.TaskStatus.objects.all()
    permission_classes = [IsAuthenticated]


class TaskImageViewSet(ModelViewSet):
    serializer_class = serializers.TaskImageSerializer
    queryset = models.TaskImage.objects.all()
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'head']


class TaskCommentViewSet(ModelViewSet):
    serializer_class = serializers.TaskCommentSerializer
    queryset = models.TaskComment.objects.all()
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'head']
