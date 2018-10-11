from rest_framework import status
from rest_framework import viewsets
from rest_framework import decorators
from rest_framework import response

from chat import models
from . import serializers


class MessageViewSet(viewsets.ModelViewSet):
    queryset = models.Message.objects.all()
    serializer_class = serializers.MessageSerializer

    @decorators.action(methods=['post'], detail=True)
    def like(self, request, pk=None):
        message = self.get_object()

        data = request.data.copy()
        data['message'] = message.pk
        serializer = serializers.MessageLikeSerializer(data=data)
        if serializer.is_valid():
            message.likes.create(author=serializer.data['author'])
            return response.Response({'likes_count': message.likes.count()})

        return response.Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST,
        )
