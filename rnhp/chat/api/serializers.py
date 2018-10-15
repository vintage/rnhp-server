from rest_framework import serializers
from rest_framework import validators

from chat import models


class MessageTypingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MessageTyping
        fields = ('author', 'updated_at')

    def create(self, validated_data):
        try:
            instance = models.MessageTyping.objects.get(
                author=validated_data['author'],
            )
        except models.MessageTyping.DoesNotExist:
            return super().create(validated_data)
        else:
            instance.save()
            return instance


class MessageSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = models.Message
        fields = ('id', 'content', 'author', 'image', 'likes_count')

    def get_likes_count(self, obj):
        return obj.likes.count()

    def create(self, validated_data):
        models.MessageTyping.objects.filter(
            author=validated_data['author'],
        ).delete()

        return super().create(validated_data)


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
