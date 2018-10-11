from rest_framework import serializers
from rest_framework import validators

from chat import models


class MessageSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = models.Message
        fields = ('id', 'content', 'author', 'likes_count')

    def get_likes_count(self, obj):
        return obj.likes.count()


class MessageLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MessageLike
        fields = ('author', 'message')
        validators = [
            validators.UniqueTogetherValidator(
                queryset=models.MessageLike.objects.all(),
                fields=('message', 'author'),
            )
        ]
