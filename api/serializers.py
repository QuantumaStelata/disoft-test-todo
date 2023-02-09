from rest_framework import serializers
from rest_framework import status

from todo import models, tasks


class TaskStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TaskStatus
        fields = "__all__"


class TaskImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TaskImage
        fields = "__all__"


class TaskCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TaskComment
        fields = "__all__"

    def create(self, validated_data):
        request = self.context.get("request")
        task = validated_data.get("task")

        user_is_author = request.user == task.author
        user_is_contributor = task.contributors.filter(id=request.user.id).exists()
        user_is_superuser = request.user.is_superuser

        if not any((user_is_author, user_is_contributor, user_is_superuser)):
            raise serializers.ValidationError({"error": "Forbidden"}, code=status.HTTP_403_FORBIDDEN)

        return super().create(validated_data)


class TaskSerializer(serializers.ModelSerializer):
    images = TaskImageSerializer(many=True, required=False)

    class Meta:
        model = models.Task
        fields = "__all__"
    
    def create(self, validated_data):
        tasks.send_email_to_users.delay([user.email for user in validated_data.get("contributors")])
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        request = self.context.get("request")

        user_is_author = request.user == instance.author
        user_is_contributor = instance.contributors.filter(id=request.user.id).exists()

        if not user_is_author and not user_is_contributor:
            raise serializers.ValidationError({"error": "Forbidden"}, code=status.HTTP_403_FORBIDDEN)
        
        if not user_is_author and user_is_contributor and (task_status := validated_data.get("status")) and task_status.id in [1, 3]:
            raise serializers.ValidationError({"error": "Forbidden"}, code=status.HTTP_403_FORBIDDEN)

        return super().update(instance, validated_data)
